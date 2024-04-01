from typing import TypeVar, Callable, Any, cast, Dict, Set
import functools
from packaging.version import parse

from .enums import HDRSeverity
from .datatypes import HDRResult
from .errors.common import InvalidVersion


def compare_version(v1: str, v2: str) -> int:
    s1 = parse(v1)
    s2 = parse(v2)
    if s1 == s2:
        return 0
    elif s1 > s2:
        return -1
    else:
        return 1


def version_lt(v1: str, v2: str) -> bool:
    return compare_version(v1, v2) > 0


def version_gte(v1: str, v2: str) -> bool:
    return not version_lt(v1, v2)


F = TypeVar('F', bound=Callable[..., Any])


def minimum_version(version: str) -> Callable[[F], F]:
    def decorator(f: F) -> F:
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            if version_lt(self._server_version, version):
                raise InvalidVersion(
                    '{0} is only available on NETLAB+ systems version {1} or later.'.format(
                        f.__name__, version
                    )
                )
            return f(self, *args, **kwargs)
        return cast(F, wrapper)
    return decorator


def hdr_result(results, severity_level=HDRSeverity.WARN) -> HDRResult:
    # TODO when card #1109 resolves, include hdr group id in response
    response: HDRResult = {
        'status': results.get('status_t'),
        'value': results.get('value'),
        'events': [],
    }
    for event in results.get('events'):
        if event['severity'] <= severity_level.value:
            response['events'].append(event)
    return response


def omit_nones(value: Dict[str, Any], names: Set[str]) -> Dict[str, Any]:
    result = {}

    for k, v in value.items():
        if v is None and k in names:
            continue
        else:
            result[k] = v

    return result
