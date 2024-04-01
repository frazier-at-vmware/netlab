from typing import Any
from typing_extensions import Protocol


class ClientProtocol(Protocol):
    _server_version: str
    async def call(self, method: str, **kwargs: Any) -> Any: ...
