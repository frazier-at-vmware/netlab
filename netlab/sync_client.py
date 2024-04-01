"""
A sync shim for compatiblity with older versions of the Netlab SDK.
"""

import logging
import asyncio
from typing import Union, Optional, Dict, Any

from .async_client import NetlabClient
from .config import NetlabServerConfig

log = logging.getLogger(__name__)


def _sync_wrap_iter(it, loop):
    try:
        while True:
            r = loop.run_until_complete(it.__anext__())
            yield r
    except StopAsyncIteration:
        pass


class SyncClient(object):
    """
    A client instance with which you can use to interact with a remote NETLAB+ system.
    """
    _async_client: NetlabClient

    def __init__(
                self,
                system: str = 'default',
                config: Union[None, NetlabServerConfig, Dict[str, Any]] = None,
                config_path: Optional[str] = None
            ):
        """
        :param system: The name to identify a NETLAB+ system. Defaults to **'default'**.
        :param config: Configuration options. See below for all possible options for the :attr:`config`.
        :param config_path: File path location of a JSON config file to be used instead of the default location.
        """
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

        self._async_client = NetlabClient(system=system, config=config, config_path=config_path)
        self._connection = self._loop.run_until_complete(self._async_client.__aenter__())

    def __repr__(self):
        return str(self._async_client)

    def __dir__(self):
        return list(super().__dir__()) + list(self._async_client._connection.__dir__())

    def __getattr__(self, name):
        from functools import wraps
        func = getattr(self._connection, name)

        @wraps(func)
        def wrapper(*args, **kwargs):
            maybe_co = func(*args, **kwargs)
            if asyncio.iscoroutine(maybe_co):
                result = self._loop.run_until_complete(maybe_co)
            else:
                result = maybe_co
            if hasattr(result, '__anext__'):
                result = _sync_wrap_iter(result, self._loop)
            return result
        return wrapper

    def disconnect(self) -> None:
        """
        Disconnect from NETLAB+.
        """
        self._loop.run_until_complete(self._async_client.__aexit__(None, None, None))
        asyncio.set_event_loop(None)
        self._loop.close()
