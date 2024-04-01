from .common import NetlabError, _add


@_add
class ContentNotFoundError(NetlabError):
    """con_id is not found."""
    str_error = "E_CONTENT_NOT_FOUND"


@_add
class ExerciseNotFoundError(NetlabError):
    """ex_id is not found."""
    str_error = "E_EXERCISE_NOT_FOUND"
