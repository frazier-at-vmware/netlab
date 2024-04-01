from enum import Enum


class PowerState(Enum):
    "Remote PC power state change."
    POWERED_ON = "POWERED_ON"
    "Remote PC has powered on."
    POWERED_OFF = "POWER_OFF"
    "Remote PC has powered off."
    SUSPEND_STARTED = "SUSPEND_STARTED"
    "Remote PC suspend started (vmware suspend)"
    SUSPENDED = "SUSPENDED"
    "Remote PC has suspended (vmware suspended)"
    RESUME_STARTED = "RESUME_STARTED"
    "Remote PC resume started (from vmware suspended state)"
    RESET_STARTED = "RESET_STARTED"
    "Remote PC reset started (hard reset)"
    GUEST_SHUTDOWN = "GUEST_SHUTDOWN"
    "Guest O/S shutdown started (graceful shutdown)"
    GUEST_REBOOT = "GUEST_REBOOT"
    "Guest O/S reboot started (graceful reboot)"
    GUEST_CRASHED = "GUEST_CRASHED"
    "Guest O/S has crashed"
    UNKNOWN = "UNKNOWN"
    "PC state can not be determined"


class CloneStorageAllocation(Enum):
    "How to allocate VM image."
    ONDEMAND = 'ONDEMAND'
    "Allocate on demand."
    PREALLOCATED = 'PREALLOCATED'
    "Preallocate."


class CloneType(Enum):
    "How to clone."
    LINKED = 'LINKED'
    "Delta of a full virtual machine."
    FULL = 'FULL'
    "Complete copy of the virtual machine."


class VirtualMachineLicenseType(Enum):
    "Virtual machine type."
    VHOST = "vhost"
    "License is for a vCenter server."
    VCENTER = "vcenter"
    "License is for a vm host server."
