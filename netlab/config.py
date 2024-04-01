"""
Config can be passed to :py:class:`netlab.async_client.NetlabClient` using environment variables,
using a json file on your system, or by passing a ``dict`` explicitly.
"""

from enum import Enum
import ssl
from typing import Optional, Union, cast
from typing_extensions import TypedDict, Literal


RAW_CIPHER_LIST = Union[None, "NetlabCipherListEnum", str]


class NetlabCipherListEnum(Enum):
    "Preconfigured Netlab cipher lists."

    NETLAB = "NETLAB"
    "Default netlab cipher list."

    @classmethod
    def get_cipher_list(cls, ciphers: RAW_CIPHER_LIST) -> Optional[str]:
        try:
            ciphers = cls[cast(str, ciphers)]
        except KeyError:
            pass

        if ciphers is cls.NETLAB:
            return "DEFAULT:AES256-GCM-SHA384"
        else:
            return ciphers


class NetlabServerConfig(TypedDict):
    """
    Passed to `netlab.async_client.NetlabClient` to configure the connection
    to a server.

    **Example**

    ::

        config = {
            "host": "192.168.1.10",
            "user": "administrator",
            "token": "S25GWP5P2247CMRDNLTCNKATT49KSGEDDPXMTM6A",
            "port": 9000,
        }

        async with NetlabClient(config=config) as client:
            ...
    """

    host: str
    "IP Address or hostname of remote NETLAB+ API."
    user: str
    "Currently ``'administrator'`` is the only user account allowed to use the API."
    token: str
    "Token obtained from NETLAB+ system."
    port: int
    "Port of remote NETLAB+ API. Usually ``9000``."
    server_hostname: Optional[str]
    "The hostname that ssl is configured to use. Only required if it is diffrent from 'host'."
    ssl: Union[Literal["default", "self_signed"], ssl.SSLContext]
    "You may pass `ssl.SSLContext` for complete control over ssl."
    ssl_ciphers: RAW_CIPHER_LIST
    "ssl ciphers to use. This can be a value from `NetlabCipherListEnum` or an openssl cipher list."
    message_byte_limit: int
    "The maximum size of a NETLAB+ message."


class NetlabServerEnvConfig(TypedDict, total=True):
    """
    Each of the above configuration options can be specified as environment variables.
    """

    NETLAB_CONFIG: str
    "Folder which contains the 'config.json'."
    NETLAB_CONFIG_HOST: str
    "IP Address or hostname of remote NETLAB+ API."
    NETLAB_CONFIG_USER: str
    "User account ID from NETLAB+ system."
    NETLAB_CONFIG_TOKEN: str
    "Token obtained from NETLAB+ system."
    NETLAB_CONFIG_PORT: str
    "Port of remote NETLAB+ API."
