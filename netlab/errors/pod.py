from .common import NetlabError, _add


@_add
class PodNotFoundError(NetlabError):
    """A pod could not be located from that request."""
    str_error = "E_POD_NOT_FOUND"


@_add
class DuplicatePodACLError(NetlabError):
    """Pod ACL already exists."""
    str_error = "E_DUPLICATE_POD_ACL"


@_add
class AdminAlreadyAuthorizedError(NetlabError):
    """acc_id is already authorized for pod_id."""
    str_error = "E_ADMIN_ALREADY_AUTHORIZED"


@_add
class ACLAdminNotFoundError(NetlabError):
    """Authorization for acc_id was not found for given pod_id."""
    str_error = "E_ACL_ADMIN_NOT_FOUND"


@_add
class PodACLNotFoundError(NetlabError):
    """pacl_uuid was not found."""
    str_error = "E_POD_ACL_NOT_FOUND"


@_add
class PodTypeNotFoundError(NetlabError):
    """pt_id was not found."""
    str_error = "E_POD_TYPE_NOT_FOUND"


@_add
class DuplicatePodIDError(NetlabError):
    """pod_id already exists."""
    str_error = "E_DUPLICATE_POD_ID"


@_add
class DuplicatePodNameError(NetlabError):
    """pod_name already exists."""
    str_error = "E_DUPLICATE_POD_NAME"


@_add
class PodMaxTypeReachedError(NetlabError):
    """Max of this pod type has been installed."""
    str_error = "E_POD_MAX_TYPE_REACHED"


@_add
class PodMaxLargeVLANReachedError(NetlabError):
    """Max number of pods with large VLANs (15) has been reached."""
    str_error = "E_POD_MAX_LARGE_VLAN_REACHED"


@_add
class PodMaxSysReachedError(NetlabError):
    """Max number of pods on this system has been reached."""
    str_error = "E_POD_MAX_SYS_REACHED"


@_add
class PodMaxDeviceReachedError(NetlabError):
    """Max number of devices has been reached."""
    str_error = "E_POD_MAX_DEVICE_REACHED"


@_add
class SourcePodNotFoundError(NetlabError):
    """The source_pod_id could not be found."""
    str_error = "E_SOURCE_POD_NOT_FOUND"


@_add
class LabDevicesNotSupportedError(NetlabError):
    """Pod cloning does not support real equipment."""
    str_error = "E_LAB_DEVICES_NOT_SUPPORTED"


@_add
class PodIDNotUniqueError(NetlabError):
    """The clone_pod_id is already in use."""
    str_error = "E_POD_ID_NOT_UNIQUE"


@_add
class PodNameNotUniqueError(NetlabError):
    """The clone_pod_name is already in use."""
    str_error = "E_POD_NAME_NOT_UNIQUE"


@_add
class NoPCCloneSpecError(NetlabError):
    """The pc_clone_spec is invalid."""
    str_error = "E_NO_PC_CLONE_SPEC"


@_add
class PCTypeNotSupportedError(NetlabError):
    """The pc_type in pc_clone_spec is not set to AVMI or NONE."""
    str_error = "E_PC_TYPE_NOT_SUPPORTED"


@_add
class SourceVirtualMachineIDRequired(NetlabError):
    """The source_vm_id in pc_clone_specs is required."""
    str_error = "E_SOURCE_VM_ID_REQUIRED"


@_add
class SourceVirtualMachineNotFoundError(NetlabError):
    """The source_vm_id in pc_clone_specs is not found."""
    str_error = "E_SOURCE_VM_NOT_FOUND"


@_add
class CloneTypeRequiredError(NetlabError):
    """The clone_type in pc_clone_specs is required."""
    str_error = "E_CLONE_TYPE_REQUIRED"


@_add
class SnapshotRequiredForLinkedCloneError(NetlabError):
    """The source_snapshot in pc_clone_specs was not set correctly."""
    str_error = "E_SNAPSHOT_REQUIRED_FOR_LINKED_CLONE"


@_add
class InvalidCloneTypeError(NetlabError):
    """The clone_type in pc_clone_specs must be set to FULL or LINKED."""
    str_error = "E_INVALID_CLONE_TYPE"


@_add
class CloneRoleRequiredError(NetlabError):
    """The clone_role in pc_clone_specs is required."""
    str_error = "E_CLONE_ROLE_REQUIRED"


@_add
class TemplateNotSupportedError(NetlabError):
    """clone_role in pc_clone_specs can not be set to TEMPLATE."""
    str_error = "E_TEMPLATE_NOT_SUPPORTED"


@_add
class VirtualMachineNameRequiredError(NetlabError):
    """The clone_name in pc_clone_specs is required."""
    str_error = "E_VM_NAME_REQUIRED"


@_add
class VirtualMachineNameInvalidError(NetlabError):
    """The clone_name in pc_clone_specs contains invalid characters."""
    str_error = "E_VM_NAME_INVALID"


@_add
class VirtualMachineNameNotUniqueLocalError(NetlabError):
    """The clone_name in pc_clone_specs is already in use."""
    str_error = "E_VM_NAME_NOT_UNIQUE_LOCAL"


@_add
class VirtualMachineNameNotUniqueGlobalError(NetlabError):
    """The clone_name in pc_clone_specs is already in use."""
    str_error = "E_VM_NAME_NOT_UNIQUE_GLOBAL"


@_add
class HostNotFoundError(NetlabError):
    """The clone_hostname in pc_clone_specs is not found."""
    str_error = "E_HOST_NOT_FOUND"


@_add
class HostOrGroupRequiredError(NetlabError):
    """The clone_vh_id in pc_clone_specs is required."""
    str_error = "E_HOST_OR_GROUP_REQUIRED"


@_add
class InvalidStorageAllocError(NetlabError):
    """The clone_storage_alloc in pc_clone_specs is not set to ONDEMAND or PREALLOCATED."""
    str_error = "E_INVALID_STORAGE_ALLOC"


@_add
class SameVirtualMachineHostRequiredError(NetlabError):
    """The source_pod_id pod type requires all VMs to be pointing to same clone_vh_id in pc_clone_specs."""
    str_error = "E_SAME_VM_HOST_REQUIRED"


@_add
class ClonePodNotFoundError(NetlabError):
    """The clone_pod_id is not found."""
    str_error = "E_CLONE_POD_NOT_FOUND"


@_add
class PodIDMismatchError(NetlabError):
    """Given pod_id does not match pc_pod_id."""
    str_error = "E_POD_ID_MISMATCH"


@_add
class PodIndexMismatchError(NetlabError):
    """Given pl_index does not match pc_pod_index."""
    str_error = "E_POD_INDEX_MISMATCH"


@_add
class VirtualMachineInUseError(NetlabError):
    """vm_id is currently in use."""
    str_error = "E_VM_IN_USE"


@_add
class PodNotOnlineError(NetlabError):
    """Current pod is not OFFLINE."""
    str_error = "E_POD_NOT_OFFLINE"


@_add
class VirtualMachineNotAttachedError(NetlabError):
    """vm_id not attached."""
    str_error = "E_VM_NOT_ATTACHED"


@_add
class PodInUseError(NetlabError):
    """Current pod is not OFFLINE."""
    str_error = "E_POD_IN_USE"


@_add
class PodActiveError(NetlabError):
    """The pod_id is not currently OFFLINE or ONLINE."""
    str_error = "E_POD_ACTIVE"


@_add
class PodNotSuspendedError(NetlabError):
    """Pod not in suspended state."""
    str_error = "E_POD_NOT_SUSPENDED"


@_add
class PodBusyError(NetlabError):
    """Pod is currently busy performing another task."""
    str_error = "E_POD_BUSY"


@_add
class PodEmptyError(NetlabError):
    """Pod has no devices or PCs."""
    str_error = "E_POD_EMPTY"


@_add
class PodNotActiveError(NetlabError):
    """Pod/reservation is not in active lab state."""
    str_error = "E_POD_NOT_ACTIVE"


@_add
class PodTypeIncompatibleError(NetlabError):
    """The pod type for the requested lab exercise is not the same as the reserved pod type."""
    str_error = "E_POD_TYPE_INCOMPATIBLE"
