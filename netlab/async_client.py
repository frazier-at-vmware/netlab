"""
`NetlabClient` is the main entrypoint to the NETLAB+ SDK.

Only `NetlabClient` should be created directly. See the mixin classes for a full list
of methods:

- :py:class:`netlab.api.ClassApiMixin`
- :py:class:`netlab.api.PodApiMixin`
- :py:class:`netlab.api.ReservationApiMixin`
- :py:class:`netlab.api.SystemApiMixin`
- :py:class:`netlab.api.LabApiMixin`
- :py:class:`netlab.api.UserApiMixin`
- :py:class:`netlab.api.VmApiMixin`

**Usage**

::

    async with NetlabClient() as client:
        client: NetlabConnection

        status = await client.system_status_get()
"""


import asyncio
import logging
import uuid
import ssl
from weakref import WeakValueDictionary
from typing import Any, Dict, Optional, NoReturn, Union, TYPE_CHECKING, cast

from .serializer import serialize, deserialize
from .auth import get_system_config
from .api import ClassApiMixin, PodApiMixin, ReservationApiMixin, SystemApiMixin, LabApiMixin, UserApiMixin, VmApiMixin
from .errors import error_decode, ResponseFormatError
from .errors.common import NetlabConnectionClosedError
from .config import NetlabServerConfig

logger = logging.getLogger(__name__)

UGLY_TASKS = {
    'vm.inventory.import.task',
    'vm.datacenter.test.task',
    'vm.datacenter.discover.vms.task',
    'vm.datacenter.discover.hosts.task',
}

if TYPE_CHECKING:  # TODO python3.9 or mypy version
    EventQueue = asyncio.Queue[asyncio.Future[Dict[str, Any]]]
    NoReturnTask = asyncio.Future[NoReturn]
    AnyFuture = asyncio.Future[Any]
else:
    EventQueue = Any
    NoReturnTask = Any
    AnyFuture = Any


__all__ = ['NetlabClient', 'NetlabConnection', 'EventStream']


class EventStream(object):
    """
    Used to collect events from a netlab subscription.

    :meta private:
    """

    def __init__(self, connection, queue):
        self._connection = connection
        self._queue = queue

    async def get(self) -> Any:
        """
        Get the next event from a subscription.
        """
        msg = await self._connection._wait_next_event(self._queue)
        return msg


class EventStreamFactory(object):
    """
    Used to create an event stream.

    :meta private:

    **Usage**

    ::

        async with NetlabClient() as client:
            async with client.subscribe('RESERVATION.ADDED') as events:
                event = await events.get()
    """

    _connection: 'NetlabConnection'
    _queue: EventQueue
    _handle: uuid.UUID
    _event: str
    _criteria: Dict[str, Any]

    def __init__(self, connection, event, criteria):
        self._connection = connection
        self._queue = asyncio.Queue()
        self._handle = uuid.uuid4()
        self._event = event
        self._criteria = criteria

    async def __aenter__(self) -> EventStream:
        self._connection._event_mapping[self._handle] = self._queue

        await self._connection.call(
            'event.subscribe',
            event=self._event,
            criteria=self._criteria,
            handle=self._handle)
        logger.debug('subscription created %s %s', self._handle, self._event)
        es = EventStream(self._connection, self._queue)

        return es

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if self._connection.alive():
            await self._connection.call('event.unsubscribe', handle=self._handle, event=self._event)
            del self._connection._event_mapping[self._handle]
            logger.debug('subscription deleted %s %s', self._handle, self._event)


class NetlabConnection(ClassApiMixin, PodApiMixin, ReservationApiMixin, SystemApiMixin, LabApiMixin,
                       UserApiMixin, VmApiMixin):
    """
    An active connection to a NETLAB+ used to communicate with it. Should only be created by a
    :py:class:`NetlabClient`.
    """
    _system_version: str
    _event_handler_task: NoReturnTask
    _keep_alive_task: NoReturnTask

    def __init__(self, reader, writer, config):
        self._reader: asyncio.StreamReader = reader
        self._writer: asyncio.StreamWriter = writer
        self._config = config
        self._event_mapping: WeakValueDictionary[uuid.UUID, EventQueue] = WeakValueDictionary()

    async def _connect(self) -> None:
        self._event_handler_task = asyncio.ensure_future(self._event_handler())
        self._keep_alive_task = asyncio.ensure_future(self._keep_alive())
        config = self._config
        await self.call('user.authenticate', user=config.user, token=config.token)
        result = await self.system_status_get()
        self._server_version = result['sys_sdn_version']

    async def _disconnect(self) -> None:
        self._writer.close()
        # await self._writer.wait_closed()
        self._keep_alive_task.cancel()
        self._event_handler_task.cancel()
        await asyncio.wait([self._event_handler_task, self._keep_alive_task])

    async def _keep_alive(self) -> NoReturn:
        while True:
            await asyncio.sleep(15)
            try:
                await asyncio.wait_for(self.call('internal.mbusd.ping'), 2.0)
            except asyncio.TimeoutError as e:
                logger.debug('keep alive packet lost')
                raise NetlabConnectionClosedError("Keep alive packet lost.") from e
            logger.debug('keep alive packet sent')

    async def _event_handler(self) -> NoReturn:
        while True:
            bmsg = await self._reader.readuntil(b'\n')
            logger.debug('data <--- %s', bmsg)

            msg = deserialize(bmsg.decode('utf-8'))

            if 'id' in msg:
                ident = uuid.UUID(msg['id'])
                payload = msg
            elif 'handle' in msg:
                ident = uuid.UUID(msg['handle'])
                payload = msg['params']
            else:
                raise ResponseFormatError('message did not contain "handle" or "id"')

            queue = self._event_mapping.get(ident)

            if queue is None:
                continue

            responder: AnyFuture = asyncio.Future()

            if 'result' in payload or 'event' in msg:
                responder.set_result(msg)
                queue.put_nowait(responder)
            elif 'error' in payload:
                responder.set_exception(error_decode(msg['error']))
                queue.put_nowait(responder)
            else:
                raise ResponseFormatError('message did not contain "result" or "error"')

    async def _call_method(self, ident: uuid.UUID, data: Dict[str, Any]) -> Any:
        msg = serialize(data)
        bmsg = msg.encode('utf-8') + b'\n'
        logger.debug('data ---> %s', bmsg)
        self._writer.write(bmsg)

        try:
            await self._writer.drain()
        except ConnectionResetError as e:
            raise NetlabConnectionClosedError() from e

        queue: EventQueue = asyncio.Queue()
        self._event_mapping[ident] = queue

        msg = await self._wait_next_event(queue)

        if 'result' in msg:
            return msg['result']
        elif msg.get('error') is not None:
            raise error_decode(msg['error'])
        else:
            raise ResponseFormatError('message did not contain "result" or "error"')

    async def _call_task(self, ident: uuid.UUID, data: Dict[str, Any]) -> Any:
        handle = uuid.uuid4()
        queue: EventQueue = asyncio.Queue()
        self._event_mapping[handle] = queue

        data['params']['notify_complete'] = True
        data['params']['notify_handle'] = handle

        await self._call_method(ident, data)

        result = await self._wait_next_event(queue)

        if 'params' not in result:
            raise ResponseFormatError('message did not contain "params"')
        msg = result['params']

        if 'result' in msg:
            return msg['result']
        elif msg.get('error') is not None:
            raise error_decode(msg['error'])
        else:
            raise ResponseFormatError('message did not contain "result" or "error"')

    async def _call_task_ugly(self, ident: uuid.UUID, data: Dict[str, Any]) -> Any:
        task_id = await self._call_method(ident, data)

        while True:
            status = await self.call('task.check', task_id=task_id)
            if status['is_complete']:
                return status['result']
            await asyncio.sleep(1)

    async def _wait_next_event(self, queue: EventQueue) -> Any:
        queue_task: AnyFuture = asyncio.ensure_future(queue.get())

        try:
            completed_tasks, _ = await asyncio.wait(
                    [queue_task, self._keep_alive_task, self._event_handler_task],
                    return_when=asyncio.FIRST_COMPLETED,
                )

            completed_task = completed_tasks.pop()

            if completed_task is queue_task:
                future = completed_task.result()
                result = await future
                return result
            else:
                raise NetlabConnectionClosedError() from completed_task.exception()
        finally:
            queue_task.cancel()
            try:
                await queue_task
            except asyncio.CancelledError:
                pass

    def alive(self) -> bool:
        return not bool(self._keep_alive_task.done() or self._event_handler_task.done())

    async def call(self, method: str, **kwargs: Any) -> Any:
        """

        :param method: The NETLAB+ method name.
        :param kwargs: The arguments to pass to netlab.

        .. warning::

            In most cases, it is better to use the higher level methods, rather than this
            low level method.
        """
        ident = uuid.uuid4()
        data = {
            'id': ident,
            'jsonrpc': '2.0',
            'method': method,
            'params': kwargs
        }

        if method in UGLY_TASKS:
            return await self._call_task_ugly(ident, data)
        elif method.endswith('.task'):
            return await self._call_task(ident, data)
        else:
            return await self._call_method(ident, data)

    def subscribe(self, event: str, **criteria: Any) -> EventStreamFactory:
        """
        Subscribe to a NETLAB+ event.

        :meta private:

        :param event: The NETLAB+ event name.
        :param critera: Any filtering criteria.

        :return: Used to accept new events.
        """

        es = EventStreamFactory(self, event, criteria)
        return es


class NetlabClient(object):
    """
    Async Context Manager for creating connections to NETLAB+.
    """
    _connection: Optional[NetlabConnection]

    def __init__(
                self,
                system: Optional[str] = 'default',
                config: Union[None, NetlabServerConfig, Dict[str, Any]] = None,  # TODO Mypy cannot infer TypedDict
                config_path: Optional[str] = None
            ):
        """
        :param system: The name to identify a NETLAB+ system. Defaults to **'default'**.
        :param config: Configuration options. See below for all possible options for the :attr:`config`.
        :param config_path: File path location of a JSON config file to be used instead of the default location.
        """
        self._config = get_system_config(system, config, config_path)
        self._connection = None

    async def __aenter__(self) -> NetlabConnection:
        assert self._connection is None
        config = self._config
        try:
            logger.debug('connecting to %s', config.host)

            ssl_context: ssl.SSLContext
            if isinstance(config.ssl, ssl.SSLContext):
                ssl_context = config.ssl
            else:
                ssl_context = ssl.create_default_context()
                if self._config.ssl_ciphers:
                    ssl_context.set_ciphers(self._config.ssl_ciphers)
                if config.ssl == 'self_signed':
                    ssl_context.check_hostname = False
                    ssl_context.verify_mode = ssl.CERT_NONE
                if cast(Any, config.ssl) not in ('default', 'self_signed'):
                    logging.warning("`ssl` should be an `ssl.SSLContext`, `'default'`, or `'self_signed'`.")

            reader, writer = await asyncio.open_connection(
                host=config.host, port=config.port, ssl=ssl_context,
                server_hostname=config.server_hostname, limit=config.message_byte_limit)
            logger.debug('tcp connection to %s', config.host)
        except ConnectionAbortedError as e:
            raise NetlabConnectionClosedError() from e
        client = NetlabConnection(reader, writer, config)
        self._connection = client
        try:
            await client._connect()
            logger.debug('completed connection to %s', config.host)
        except Exception:
            await client._disconnect()
            raise
        return client

    async def __aexit__(self, exc_type, exc_value, traceback):
        assert self._connection, "__aexit__ called without __aenter__"
        await self._connection._disconnect()
        self._connection = None
        logger.debug('successfully disconnected from %s', self._config.host)
