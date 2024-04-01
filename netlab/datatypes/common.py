from datetime import datetime
from typing_extensions import TypedDict
from typing import Any, List
from ..enums import HDRStatus, HDRSeverity


class HDREvent(TypedDict):
    time: datetime
    msg: str
    code: str
    severity: HDRSeverity


class HDRResult(TypedDict):
    status: HDRStatus
    value: Any
    events: List[HDREvent]
