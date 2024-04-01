from .common import NetlabError, _add


@_add
class AlreadyRegisteredError(NetlabError):
    """Content is already registered to class."""
    str_error = "E_ALREADY_REGISTERED"


@_add
class ClassNotFoundError(NetlabError):
    """Requested cls_id was not found."""
    str_error = "E_CLASS_NOT_FOUND"


@_add
class NotRegisteredError(NetlabError):
    """con_id not registered in class."""
    str_error = "E_NOT_REGISTERED"


@_add
class AccountNotInstructorError(NetlabError):
    """acc_id cannot be set to lead."""
    str_error = "E_ACCOUNT_NOT_INSTRUCTOR"


@_add
class AlreadyMemberError(NetlabError):
    """acc_id is already a member of class."""
    str_error = "E_ALREADY_MEMBER"


@_add
class NotMemberError(NetlabError):
    """acc_id is not on roster."""
    str_error = "E_NOT_MEMBER"


@_add
class RemoveLastLeadError(NetlabError):
    """Returned more than one lead."""
    str_error = "E_REMOVE_LAST_LEAD"
