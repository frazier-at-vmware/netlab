"Common and Base errors"

from typing import Optional, Type, List

CODES: List[Type['NetlabError']] = []


class NetlabConnectionClosedError(Exception):
    pass


class ResponseFormatError(Exception):
    """The server's response was impossible to decode."""


class InvalidConfig(Exception):
    """Config is not readable or contains errors."""


class InvalidVersion(Exception):
    """The remote API version is not compatible."""


class NetlabError(Exception):
    """Base error from NETLAB+ api."""
    str_error = "E_NETLAB_ERROR"
    message: Optional[str]

    def __init__(self, message: Optional[str] = None):
        self.message = message

    def __str__(self) -> str:
        if self.message is None:
            return "[{}]".format(self.str_error)
        else:
            return '[{}] {}'.format(self.str_error, self.message)


class AuthenticationError(NetlabError):
    """Connection to the NETLAB+ system could not be authenticated."""
    str_error = "E_AUTHENTICATION_FAILED"


class UnmappedError(NetlabError):
    """An Error returned by the server but not handled by this library."""
    def __init__(self, str_error: str, message: Optional[str]):
        self.str_error = str_error
        self.message = message


def _add(cls: Type[NetlabError]) -> Type[NetlabError]:
    CODES.append(cls)
    return cls


@_add
class MethodNotFoundError(NetlabError):
    """The requested method could not be found."""
    str_error = "E_METHOD_NOT_FOUND"


@_add
class ParamsNotSupported(NetlabError):
    """Some parameters were incorrect."""
    str_error = "E_PARAMS_NOT_SUPPORTED"


@_add
class MissingParamError(NetlabError):
    """Parameter was missing."""
    str_error = "E_MISSING_PARAM"


@_add
class MissingParamsError(NetlabError):
    """Parameter was missing."""
    str_error = "E_MISSING_PARAMS"


@_add
class InvalidParamsError(NetlabError):
    """Parameters are in some way incorrect."""
    str_error = "E_INVALID_PARAMS"


@_add
class InvalidParamError(NetlabError):
    """Parameter is in some way incorrect."""
    str_error = "E_INVALID_PARAM"


@_add
class InvalidFilterError(NetlabError):
    """Filter is not a valid filter."""
    str_error = "E_FILTER_INVALID"


@_add
class InvalidFilterPropertyError(NetlabError):
    """Filter contains an invalid property or operator."""
    str_error = "E_FILTER_PROPERTY"


@_add
class AccessDeniedError(NetlabError):
    """Caller did not have required privilege."""
    str_error = "E_ACCESS_DENIED"


@_add
class DatesEndBeforeStartError(NetlabError):
    """End date is before start date."""
    str_error = "E_DATES_END_BEFORE_START"


@_add
class ItemDependencyError(NetlabError):
    """The virtual machine is in use by a pod."""
    str_error = "E_ITEM_DEPENDENCY"


@_add
class InvalidTimeError(NetlabError):
    """The time format provided does not match yyy-mm-dd-hh-ss."""
    str_error = "E_INVALID_TIME"


@_add
class TaskNotFoundError(NetlabError):
    """task_id is not found."""
    str_error = "E_TASK_NOT_FOUND"


@_add
class InvalidPropertiesError(NetlabError):
    """The properties requested could not be found."""
    str_error = "E_INVALID_PROPERTIES"


@_add
class LicenseNotActiveError(NetlabError):
    """Software license is not active."""
    str_error = "E_LICENSE_NOT_ACTIVE"
