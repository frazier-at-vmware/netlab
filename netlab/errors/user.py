from .common import NetlabError, _add


@_add
class CommunityNotFoundError(NetlabError):
    """A pod could not be located from that request."""
    str_error = "E_COMMUNITY_NOT_FOUND"


@_add
class NameNotUniqueError(NetlabError):
    """acc_user_id already exists in the community."""
    str_error = "E_NAME_NOT_UNIQUE"


@_add
class ClassCommunityMismatchError(NetlabError):
    """cls_id exists but is not in com_id."""
    str_error = "E_CLASS_COMMUNITY_MISMATCH"


@_add
class ClassNotLeadError(NetlabError):
    """Requester acc_id must be a class lead."""
    str_error = "E_CLASS_NOT_LEAD"


@_add
class DatabaseInsertFailedError(NetlabError):
    """Unable to insert record."""
    str_error = "E_DB_INSERT_FAILED"


@_add
class PasswordRequiredError(NetlabError):
    """new_password is required."""
    str_error = "E_PASSWORD_REQUIRED"


@_add
class PasswordTooShortError(NetlabError):
    """new_password is < 7."""
    str_error = "E_PASSWORD_TOO_SHORT"


@_add
class PasswordTooLongError(NetlabError):
    """new_password is > 64."""
    str_error = "E_PASSWORD_TOO_LONG"


@_add
class PasswordLeadingWhitespaceError(NetlabError):
    """There is whitespace before new_password."""
    str_error = "E_PASSWORD_LEADING_WHITESPACE"


@_add
class PasswordTrailingWhitespaceError(NetlabError):
    """There is whitespace after new_password."""
    str_error = "E_PASSWORD_TRAILING_WHITESPACE"


@_add
class PasswordUniqueCharsError(NetlabError):
    """new_password requires at least 5 unique characters."""
    str_error = "E_PASSWORD_UNIQUE_CHARS"


@_add
class PasswordIsCurrentError(NetlabError):
    """new_password is the same as current password."""
    str_error = "E_PASSWORD_IS_CURRENT"


@_add
class PasswordIsUserIdError(NetlabError):
    """new_password is the same as user id."""
    str_error = "E_PASSWORD_IS_USERID"


@_add
class PasswordIsFamilyNameError(NetlabError):
    """new_password is the same as account family name."""
    str_error = "E_PASSWORD_IS_FAMILY_NAME"


@_add
class PasswordIsGivenNameError(NetlabError):
    """new_password is the same as account given name."""
    str_error = "E_PASSWORD_IS_GIVEN_NAME"


@_add
class PasswordIsFullNameError(NetlabError):
    """new_password is the same as account full name."""
    str_error = "E_PASSWORD_IS_FULL_NAME"


@_add
class PasswordIsEmailError(NetlabError):
    """new_password is the same as account email."""
    str_error = "E_PASSWORD_IS_EMAIL"


@_add
class DictionaryError(NetlabError):
    """Could not access the common word dictionary."""
    str_error = "E_DICTIONARY_ERROR"


@_add
class PasswordCommonError(NetlabError):
    """new_password is a common word."""
    str_error = "E_PASSWORD_COMMON"


@_add
class AccountNotFoundError(NetlabError):
    """acc_id not found."""
    str_error = "E_ACCOUNT_NOT_FOUND"


@_add
class UserIdRequiredError(NetlabError):
    """user_id is required."""
    str_error = "E_USER_ID_REQUIRED"


@_add
class UserIdReserveredError(NetlabError):
    """The following names are reserved for NDG and NETLAB+, administrator system techsupport"""
    str_error = "E_USER_ID_RESERVED"


@_add
class UserIdNotUniqueError(NetlabError):
    """This name is already in use."""
    str_error = "E_USER_ID_NOT_UNIQUE"


@_add
class InvalidUserIdError(NetlabError):
    """user_id is invalid."""
    str_error = "E_INVALID_USER_ID"


@_add
class LoginsDisabledSystemError(NetlabError):
    """Logins have been disabled globally on system."""
    str_error = "E_LOGINS_DISABLED_SYSTEM"


@_add
class SystemTerminatedError(NetlabError):
    """System was terminated by NDG."""
    str_error = "E_SYSTEM_TERMINATED"


@_add
class InvalidSessionError(NetlabError):
    """acc_session_id is invalid."""
    str_error = "E_INVALID_SESSION"


@_add
class InvalidTransactionError(NetlabError):
    """TX number invalid."""
    str_error = "E_INVALID_TRANSACTION"
