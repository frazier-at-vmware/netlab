from typing import Dict, Union, Optional, NamedTuple, Any, List
from typing_extensions import Literal
import json
import ssl
import logging
import os
import warnings
from ipaddress import ip_address
from pathlib import Path

from .errors.common import InvalidConfig
from .config import NetlabCipherListEnum

ENV_PREFIX = 'NETLAB_CONFIG_'
ENV_BOOLEANS: List[str] = []
CONFIG_FILENAME = os.path.join('.netlab', 'config.json')
DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser('~'), CONFIG_FILENAME)
log = logging.getLogger(__name__)


class SystemConfig(NamedTuple):
    user: str
    token: str
    host: str
    port: int
    ssl: Union[ssl.SSLContext, Literal['default', 'self_signed']]
    ssl_ciphers: str
    server_hostname: Optional[str]
    message_byte_limit: int


def get_system_config(system, config=None, config_path=None) -> SystemConfig:
    defaults: Any = {
        'host': 'localhost',
        'port': 9000,
        'ssl': 'default',
        'server_hostname': None,
        'message_byte_limit': 1024 * 1024 * 64,
        'ssl_ciphers': 'NETLAB',
    }

    if config:
        # config from Client init
        defaults.update(config)
    else:
        # file config
        defaults.update(load_config(system, config_path))

        # environment variables config
        env_vars = [(k, v) for (k, v) in os.environ.items() if k.startswith(ENV_PREFIX)]
        if env_vars:
            env_config: Dict[str, Union[str, bool]] = {}
            for k, v in env_vars:
                key = k.replace(ENV_PREFIX, '').lower()
                if key in ENV_BOOLEANS:
                    # convert env value to python boolean
                    env_config[key] = v.lower() in ("true", "yes", "t", "1")
                else:
                    env_config[key] = v
            defaults.update(env_config)

    try:
        ip = ip_address(defaults['host'])
    except ValueError:
        ip = None

    if defaults['server_hostname'] is None and ip is not None and defaults['ssl']:
        warnings.warn("You have passed an ip address without a 'server_hostname'. This is insecure.")
        defaults['server_hostname'] = ''
    if 'user' not in defaults:
        raise InvalidConfig('Config missing required "user".')
    if 'token' not in defaults:
        raise InvalidConfig('Config missing required "token".')
    if 'timeout' in defaults:
        defaults.pop('timeout')
        warnings.warn('Config contains `timeout`, which is deprecated.', DeprecationWarning)
    if not defaults['ssl']:
        warnings.warn('SSL is not being used, this is insecure.', DeprecationWarning)

    defaults['ssl_ciphers'] = NetlabCipherListEnum.get_cipher_list(defaults['ssl_ciphers'])

    return SystemConfig(**defaults)


def load_config(system=None, config_path=None):
    """
    Loads authentication data from a Netlab configuration file in the given
    root directory or if config_path is passed use given path.
    If no system is specified, return entire config dict.
    Lookup priority:
        explicit config_path parameter > NETLAB_CONFIG environment variable > ~/.netlab/config.json
    """
    config_file = find_config_file(config_path)

    if not config_file or not config_file.exists():
        return {}

    try:
        with open(config_file) as f:
            data = json.load(f)
            if system:
                return data.get(system, {})
            else:
                return data
    except (IOError, KeyError, ValueError) as e:
        log.debug(e)
        raise


def add_config(system, config, config_path=None):
    """
    Adds system and config data from a Netlab to the configuration file
    """
    current_config = load_config(config_path=config_path)
    current_config[system] = config
    config_file = find_config_file(config_path)
    if not config_file:
        env_path = os.environ.get('NETLAB_CONFIG')
        if env_path:
            config_file = Path(env_path) / 'config.json'
        else:
            config_file = Path(DEFAULT_CONFIG_PATH)

    try:
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(current_config, f, sort_keys=True, indent=4)
    except (IOError, KeyError, ValueError) as e:
        log.debug(e)
        raise


def remove_config(system, config_path=None):
    """
    Removes system and config data from the configuration file
    """
    current_config = load_config(config_path=config_path)
    if not system:
        current_config = {}
    else:
        current_config.pop(system, None)

    config_file = find_config_file(config_path)

    try:
        with open(config_file, 'w') as f:
            json.dump(current_config, f, sort_keys=True, indent=4)
    except (IOError, KeyError, ValueError) as e:
        log.debug(e)
        raise


def find_config_file(config_path: Optional[str] = None) -> Path:
    netlab_config_path = os.environ.get('NETLAB_CONFIG')

    environment_path = os.path.join(
        netlab_config_path,
        os.path.basename(CONFIG_FILENAME)
    ) if netlab_config_path else None

    paths = filter(None, [
        config_path,
        environment_path,
        DEFAULT_CONFIG_PATH
    ])

    return Path(next(paths))
