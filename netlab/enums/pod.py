from enum import Enum


class PodCategory(Enum):
    """
    Pod category type.
    """
    REAL_EQUIPMENT = 'RE'
    "Real Equipment Pod (i.e. Cisco Equipment)"
    PERSISTENT_VM = 'PV'
    "Persistent VM Pod"
    EPHEMERAL_VM = 'EV'
    "Ephemeral VM Pod"
    MASTER_VM = 'MV'
    "Master VM Pod"
    NORMAL_VM = 'NV'
    "Normal VM Pod"


class PCIcon(Enum):
    """
    Icon Identifier
    """
    PC = "P"
    "PC"
    SERVER = "S"
    "Server"


class PCType(Enum):
    """
    PC Type.
    """
    ABSENT = "ABSENT"
    "PC is absent."
    AVMI = "AVMI"
    "PC is in virtual machine inventory."


class PLIcon(Enum):
    """
    Pod design PC icon identifier.
    """
    PC = "P"
    "PC"
    SERVER = "S"
    "Server"


class VirtualHostComPath(Enum):
    """
    Virtual host communication path.
    """
    OUTSIDE = 'OUTSIDE'
    "Communication will be done on the OUTSIDE network."
    INSIDE = 'INSIDE'
    "Communication will be done on the INSIDE (169.254.0.x) network."


class VirtualMachineRole(Enum):
    """
    Virtual machine role in NETLAB+ inventory.
    """
    NORMAL = 'NORMAL'
    "Virtual machine will typically revert to snapshot after reservation."
    MASTER = 'MASTER'
    """
    Virtual machine is often associated with the Master Pod. Additional protections are in place
    to prevent accidental removal.
    """
    PERSISTENT = 'PERSISTENT'
    """
    Virtual machine will not revert to snapshot after reservation.
    """
    TEMPLATE = 'TEMPLATE'
    """
    Pristine virtual machine image used as the basis for cloning many virtual machines.
    Template VMs cannot be powered on, modified, or assigned to pods.
    """


class PodState(Enum):
    """
    PC Pod State
    """
    ONLINE = 'ONLINE'
    "Online."
    OFFLINE = 'OFFLINE'
    "Offline"
    RESUME = 'RESUME'
    "Resume"


class RemoveVMS(Enum):
    """
    How to remove VMs during pod removal.
    """
    NONE = 'NONE'
    "None"
    LOCAL = 'LOCAL'
    "Local"
    DATACENTER = 'DATACENTER'
    "Datacenter"
    DISK = 'DISK'
    "Disk"


class PodAdminState(Enum):
    """
    This enumeration describes the administrative states of a pod.

    The administrative state is the state that is desired, not necessarily the current running
    state (:py:class:`netlab.enums.PodAdminState`).
    """
    OFFLINE = "OFFLINE"
    "Pod is offline and idle."
    ONLINE = "ONLINE"
    "Pod is online and idle."
    ACTIVE_INIT = "ACTIVE_INIT"
    "Pod is active and initializing."
    ACTIVE_LOAD = "ACTIVE_LOAD"
    "Pod is active and loading configuration."
    ACTIVE_LAB = "ACTIVE_LAB"
    "Pod is active and available for user interaction."
    ACTIVE_POST = "ACTIVE_POST"
    "Pod is active but no longer available for interaction."
    ACTIVE_SAVE = "ACTIVE_SAVE"
    "Pod is active and saving state."
    ACTIVE_TERM = "ACTIVE_TERM"
    "Pod is active and cleaning up."
    CLONING = "CLONING"
    "Pod is in the process of being cloned."
    SUSPENDED = "SUSPENDED"
    "Pod is suspended due to errors."
    RESUME = "RESUME"
    "Pod is resuming from a suspended state."


class PodCurrentState(Enum):
    """
    This enumeration describes the possible running states of a pod.
    """
    OFFLINE = "OFFLINE"
    "Pod is offline and idle."
    ONLINE = "ONLINE"
    "Pod is online and idle."
    ACTIVE_INIT = "ACTIVE_INIT"
    "Pod is active and initializing."
    ACTIVE_LOAD = "ACTIVE_LOAD"
    "Pod is active and loading configuration."
    ACTIVE_LAB = "ACTIVE_LAB"
    "Pod is active and available for user interaction."
    ACTIVE_POST = "ACTIVE_POST"
    "Pod is active but no longer available for interaction."
    ACTIVE_SAVE = "ACTIVE_SAVE"
    "Pod is active and saving state."
    ACTIVE_TERM = "ACTIVE_TERM"
    "Pod is active and cleaning up."
    CLONING = "CLONING"
    "Pod is in the process of being cloned."
    SUSPENDED = "SUSPENDED"
    "Pod is suspended due to errors."
    RESUME = "RESUME"
    "Pod is resuming from a suspended state."
