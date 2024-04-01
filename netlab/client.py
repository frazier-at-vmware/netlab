import warnings
from .sync_client import SyncClient as Client

warnings.filterwarnings("default", category=DeprecationWarning)

warnings.warn(
    "'Client' is deprecated. Use 'netlab.sync_client.SyncClient' or 'netlab.async_client.NetlabClient'",
    DeprecationWarning
)

__all__ = ['Client']
