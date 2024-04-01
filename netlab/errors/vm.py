from .common import NetlabError, _add


@_add
class VirtualMachineIsTemplateError(NetlabError):
    """Virtual machine role is a template."""
    str_error = "E_VM_IS_TEMPLATE"


@_add
class VirtualMachineIsPersistentError(NetlabError):
    """Virtual machine role is persistent."""
    str_error = "E_VM_IS_PERSISTENT"


@_add
class VirtualMachineIsRuntimeError(NetlabError):
    """Virtual machine role is runtime."""
    str_error = "E_VM_IS_RUNTIME"


@_add
class VirtualMachineSnapshotRequiredError(NetlabError):
    """snapshot_id or snapshot_name is required."""
    str_error = "E_VM_SNAPSHOT_REQUIRED"


@_add
class VirtualMachineToolsUnavailableError(NetlabError):
    """VMWare tools are unavailable."""
    str_error = "E_VM_TOOLS_UNAVAILABLE"


@_add
class VirtualMachineShutdownTimeoutError(NetlabError):
    """The virtual machine did not shutdown within wait_seconds seconds."""
    str_error = "E_VM_SHUTDOWN_TIMEOUT"


@_add
class VirtualMachineInvalidHostError(NetlabError):
    """Could not determine runtime host from virtual machine."""
    str_error = "E_VM_INVALID_HOST"


@_add
class VirtualMachineHostNotFoundError(NetlabError):
    """vh_id not found."""
    str_error = "E_VM_HOST_NOT_FOUND"


@_add
class InternalError(NetlabError):
    """VM pc_id not the same as inventory pc_id."""
    str_error = "E_INTERNAL_ERROR"


@_add
class VirtualMachineWrongHostError(NetlabError):
    """vm_id is powered up on incorrect host."""
    str_error = "E_VM_WRONG_HOST"


@_add
class VirtualMachineInvalidPowerStateError(NetlabError):
    """If ok_if_on is not set, then VM was already powered on."""
    str_error = "E_VM_INVALID_POWER_STATE"


@_add
class VirtualMachineDatacenterMismatchError(NetlabError):
    """vm_id and vh_id not in the same datacenter."""
    str_error = "E_VM_DATACENTER_MISMATCH"


@_add
class InvalidParametersError(NetlabError):
    """"""
    str_error = "E_INVALID_PARAMETERS"


@_add
class PCNotFoundError(NetlabError):
    """pc_id is not found."""
    str_error = "E_PC_NOT_FOUND"


@_add
class VirtualMachineNotFoundError(NetlabError):
    """vm_id could not be found."""
    str_error = "E_VM_NOT_FOUND"


@_add
class VirtualMachineDatacenterNotFoundError(NetlabError):
    """vdc_id not found."""
    str_error = "E_VM_DATACENTER_NOT_FOUND"


@_add
class VirtualMachineDatacenterNotUniqueError(NetlabError):
    """vdc_id not unique."""
    str_error = "E_VM_DATACENTER_NOT_UNIQUE"


VirtualMachineDatacenterNotFoundUnique = VirtualMachineDatacenterNotUniqueError
# Backwards compatiblity TODO Remove on major version.


@_add
class VirtualMachineInvalidStateError(NetlabError):
    """Virtual machine is not currently connected."""
    str_error = "E_VM_INVALID_STATE"


@_add
class VirtualMachineNotUniqueError(NetlabError):
    """Duplicate vm_uuid in datacenter vdc_id."""
    str_error = "E_VM_NOT_UNIQUE"


@_add
class VirtualMachineParentNotFoundError(NetlabError):
    """vm_parent_id is not found."""
    str_error = "E_VM_PARENT_NOT_FOUND"


@_add
class VirtualMachineHostInvalidNameError(NetlabError):
    """vh_name is invalid."""
    str_error = "E_VM_HOST_INVALID_NAME"


@_add
class VirtualMachineHostNotUniqueError(NetlabError):
    """vh_name is not unique."""
    str_error = "E_VM_HOST_NOT_UNIQUE"


@_add
class DataBaseUpdateFailedError(NetlabError):
    """Database error."""
    str_error = "E_DB_UPDATE_FAILED"


@_add
class ValueRequiredError(NetlabError):
    """vdc_name is required."""
    str_error = "E_VALUE_REQUIRED"


@_add
class ValueIsBlankError(NetlabError):
    """vdc_name can not be blank."""
    str_error = "E_VALUE_IS_BLANK"


@_add
class ValueNotWebsafeError(NetlabError):
    """vdc_name is not web safe."""
    str_error = "E_VALUE_NOT_WEBSAFE"


@_add
class VDCMONStopError(NetlabError):
    """Could not stop vdcmon for vdc_id."""
    str_error = "E_VDCMON_STOP"


@_add
class VirtualMachineDatacenterInvalidHostnameError(NetlabError):
    """vdc_agent_hostname is invalid."""
    str_error = "E_VM_DATACENTER_INVALID_HOSTNAME"


@_add
class VirtualMachineDatacenterInvalidTypeError(NetlabError):
    """vdt_type is invalid."""
    str_error = "E_VM_DATACENTER_INVALID_TYPE"


@_add
class VirtualMachineNotAVMI(NetlabError):
    """Virtual machine is a template."""
    str_error = "E_VM_NOT_AVMI"


@_add
class VirtualMachineSnapshotCurrentNotFoundError(NetlabError):
    """Could not revert VM image to current snapshot, a current snapshot does not exist."""
    str_error = "E_VM_SNAPSHOT_CURRENT_NOT_FOUND"


@_add
class VirtualMachineHostPortGroupNotFoundError(NetlabError):
    """Could not map portgroup.id to portgroup name. Portgroup does not exist on host."""
    str_error = "E_VM_HOST_PORTGROUP_NOT_FOUND"


@_add
class VirtualMachineInvalidDeviceError(NetlabError):
    """Network adapter vnic does not exist on this vm."""
    str_error = "E_VM_INVALID_DEVICE"


@_add
class VirtualMachineHostGroupNotMemberError(NetlabError):
    """clone_vh_id is not a part of clone_vhg_id."""
    str_error = "E_VM_HOST_GROUP_NOT_MEMBER"


@_add
class VirtualMachineHostGroupEmptyError(NetlabError):
    """clone_vhg_id is empty."""
    str_error = "E_VM_HOST_GROUP_EMPTY"


@_add
class DatacenterMismatchError(NetlabError):
    """Host clone_vh_id is not in parent datacenter vdc_id."""
    str_error = "E_DATACENTER_MISMATCH"
