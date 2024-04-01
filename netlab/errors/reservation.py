from .common import NetlabError, _add


@_add
class ReservationNotFoundError(NetlabError):
    """res_id is not found."""
    str_error = "E_RESERVATION_NOT_FOUND"


@_add
class ReservationCompletedError(NetlabError):
    """Reservation is already completed."""
    str_error = "E_RESERVATION_COMPLETED"


@_add
class ReservationNotActiveError(NetlabError):
    """res_id is not currently active."""
    str_error = "E_RESERVATION_NOT_ACTIVE"


@_add
class DateEndNotSlotError(NetlabError):
    """The specified end_time must be on a time slot boundary."""
    str_error = "E_DATE_END_NOT_SLOT"


@_add
class DateEndBeforeStartError(NetlabError):
    """The specified end_time is before start_time."""
    str_error = "E_DATE_END_BEFORE_START"


@_add
class TimeEndPassedError(NetlabError):
    """The specified end_time has already passed."""
    str_error = "E_TIME_END_PASSED"


@_add
class ReservationTimeTooShortError(NetlabError):
    """The length of the reservation is too short."""
    str_error = "E_RESERVATION_TIME_TOO_SHORT"


@_add
class DateOutOfRangeError(NetlabError):
    """Reservation is outside of dates defined for the cls_id."""
    str_error = "E_DATE_OUT_OF_RANGE"


@_add
class ClassNotMemberError(NetlabError):
    """acc_id is not part of cls_id."""
    str_error = "E_CLASS_NOT_MEMBER"


@_add
class ReservationTimeTooLongError(NetlabError):
    """Reservation is longer than the max time allowed."""
    str_error = "E_RESERVATION_TIME_TOO_LONG"


@_add
class ClassNoTeamMembersError(NetlabError):
    """There are no members in team."""
    str_error = "E_CLASS_NO_TEAM_MEMBERS"


@_add
class AccessTypeError(NetlabError):
    """Account acc_id is not an instructor."""
    str_error = "E_ACCESS_TYPE"


@_add
class PodNotAvailableError(NetlabError):
    """Pod is filtered out by pod assignment."""
    str_error = "E_POD_NOT_AVAILABLE"


@_add
class ReservationTimeMTBRError(NetlabError):
    """The minimum time between reservations has not been exceeded."""
    str_error = "E_RESERVATION_TIME_MTBR"


@_add
class ReservationConflictPodError(NetlabError):
    """This reservation conflicts with another reservation."""
    str_error = "E_RESERVATION_CONFLICT_POD"


@_add
class ReservationActivePodMaxError(NetlabError):
    """This reservation exceeds the max active pod limit."""
    str_error = "E_RESERVATION_ACTIVE_POD_MAX"


@_add
class ReservationPodRulesError(NetlabError):
    """Pod rules do not alow this reservation."""
    str_error = "E_RESERVATION_POD_RULES"


@_add
class ReservationActivePCMaxError(NetlabError):
    """This reservation exceeds the max active pc limit."""
    str_error = "E_RESERVATION_ACTIVE_PC_MAX"


@_add
class ReservationPRAMaxVirtualMachineError(NetlabError):
    """This reservation exceeds the max number of VMs for this host set by PRA."""
    str_error = "E_RESERVATION_PRA_MAX_VM"


@_add
class ReservationPRAMaxCPUError(NetlabError):
    """This reservation exceeds the max number of CPUs for this host set by PRA."""
    str_error = "E_RESERVATION_PRA_MAX_CPU"


@_add
class ReservationPRAMaxMemoryError(NetlabError):
    """This reservation exceeds the max amount of RAM for this host set by PRA."""
    str_error = "E_RESERVATION_PRA_MAX_MEM"


@_add
class ReservationTimeInsufficientError(NetlabError):
    """Not enough time remaining to complete operation."""
    str_error = "E_RESERVATION_TIME_INSUFFICIENT"
