"""
Datatypes for working with a vm.
"""

from typing_extensions import TypedDict
from typing import Dict, Optional, List


class VMAllocTotal(TypedDict):
    vm_n_vms: int
    "Total number of virtual machines in this pod. Remote PCs of type ABSENT are not counted."
    vm_n_cpu: int
    "Total number of virtual CPUs consumed by this pod."
    vm_mem_mb: int
    "Total amount of RAM allocated to all VMs in this pod (megabytes)."


class VMAllocHostInfo(TypedDict):
    vm_n_vms: int
    "Total number of virtual machines of the pod assigned to this host."
    vm_n_cpu: int
    "Total number of virtual CPUs consumed by this pod on this host."
    vm_mem_mb: int
    "Total amount of RAM (megabytes) allocated by VMs in this pod on this host."
    vh_pra_enabled: bool
    "Proactive Resource Awareness is enabled on this host."
    vh_pra_max_vm: Optional[bool]
    """Maximum number of virtual machines allowed to be scheduled on this host when PRA enabled.
    `None` if PRA is disabled."""
    vh_pra_max_cpu: Optional[bool]
    """Maximum number of virtual CPUs allowed to be scheduled on this host when PRA enabled.
    None if PRA is disabled."""
    vh_pra_max_mem_mb: Optional[bool]
    """Maximum amount of memory that can be scheduled on this host when PRA enabled.
    None if PRA is disabled."""


class VMAlloc(TypedDict):
    """
    VMAlloc contains information about potential VM resource consumption in a given pod.
    """
    total: VMAllocTotal
    """
    Contains total number of virtual machines, virtual CPUs, and memory allocation of the
    entire pod.
    """
    vh_ids: List[int]
    """
    List of vh_id host identifiers of the virtual machine hosts assigned to the pod's VMs.
    May be empty list if the pod has not yet been assigned to any hosts. If list contains
    one host identifier, then all VMs in the pod are assigned to the same host.
    """
    vh_alloc: Dict[str, VMAllocHostInfo]
    """
    Dict containing number of virtual machines, virtual CPUs, and memory allocation for each host
    assigned to the pod. The keys of vh_alloc are vh_id host identifiers; each key is also be a
    member of the vh_ids list. The values of this dict are type VM_Alloc_HostInfo (see below).
    May be an empty dict if the pod has not yet been assigned to any hosts.
    """
