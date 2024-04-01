from typing_extensions import TypedDict, Literal
from typing import Optional


class PCCloneSpec(TypedDict, total=False):
    "Instructions for a clone."
    clone_datastore: str
    "The name of the datastore the cloned VM will reside."
    clone_name: str
    "Cloned VM name. Default: {clone_pod_name}_{pc_label}"
    clone_role: Literal['MASTER', 'NORMAL', 'PERSISTENT', 'TEMPLATE']
    """
    :MASTER: Commonly used for master pod deployment. Can not be easily deleted.
    :NORMAL: *Default* Standard virtual machine image for use in pods.
    :PERSISTENT: Commonly used when the virtual machine is not reverting to snapshot and is perpetual.
    :TEMPLATE: Pristine virtual machine image used as the basis for cloning many virtual machines.
        Template VMs cannot be powered on, modified, or assigned to pods.
    """
    clone_snapshot: Optional[str]
    """Name of the snapshot to take on cloned VM. GOLDEN_MASTER is recommended. If not set, a
    snapshot will not be taken of the cloned VM."""
    clone_storage_alloc: Literal['ONDEMAND', 'PREALLOCATED']
    """
    :ONDEMAND: *Default* Actual size of disk will grow as data is added (saves on storage).
    :PREALLOCATED: The entire disk size will be allocated immediately.
    """
    clone_type: Literal['LINKED', 'FULL']
    """
    :LINKED: *Default* Linked clone is a delta of a full virtual machine.
    :FULL: Full clone is a complete copy of the virtual machine.
    """
    clone_vh_id: int
    "The runtime host of cloned VM."
    copy_bios_uuid: bool
    "If true, copy this VMs BIOS UUID to any VM cloned from this one."
    pc_type: Literal['AVMI', 'ABSENT']
    """
    :AVMI: Use virtual machine inventory.
    :ABSENT: PC is absent.
    """
    pl_index: int
    "PC index of the pod design."
    source_snapshot: str
    "Source VM snapshot name. Default: vm_snapshot"
    source_vm_id: str
    "Source VM pod identifier."
