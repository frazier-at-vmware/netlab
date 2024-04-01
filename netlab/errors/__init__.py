"Errors that may be returned by Netlab or the Netlab SDK."

from typing import Dict, Type, Optional

from .common import UnmappedError, ResponseFormatError, NetlabError
from . import klass, lab, pod, reservation, user, vm  # noqa: F401


def _construct_mapping() -> Dict[str, Type[NetlabError]]:
    from .common import CODES, NetlabError

    result: Dict[str, Type[NetlabError]] = {}
    for code in CODES:
        assert code.str_error not in result, code.str_error
        result[code.str_error] = code

    return result


NAME_CODE_MAPPING = _construct_mapping()


def error_decode(e):
    if isinstance(e, str):
        error_code = e
        error_data: Optional[str] = None
    elif not isinstance(e, dict):
        return ResponseFormatError()
    else:
        error_code = e['message']
        try:
            error_data = e['data']['message']
        except KeyError:
            error_data = None

    if error_code in NAME_CODE_MAPPING:
        return NAME_CODE_MAPPING[error_code](error_data)
    else:
        return UnmappedError(error_code, error_data)
