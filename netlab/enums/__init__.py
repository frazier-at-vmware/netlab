"""
Netlab enums.
"""

from .common import TimeFormat, DateFormat, HDRSeverity, HDRStatus

from .klass import ClassEmailLogs, ClassLabLimit, ClassExtensionSlots, ContentAccessiblity
from .pod import (
    PCIcon, PCType, PLIcon, PodCategory, PodState, RemoveVMS, VirtualHostComPath, VirtualMachineRole,
    PodAdminState, PodCurrentState
)
from .reservation import ReservationType, ReservationScope, InitConfig
from .user import AccountPrivileges, AccountType, CommunityExtensionSlots
from .vm import PowerState, CloneStorageAllocation, CloneType, VirtualMachineLicenseType

__all__ = (
    'TimeFormat', 'DateFormat', 'HDRSeverity', 'HDRStatus',

    'ClassEmailLogs', 'ClassLabLimit', 'ClassExtensionSlots',

    'PCIcon', 'PCType', 'PLIcon', 'PodCategory', 'PodState', 'RemoveVMS', 'VirtualHostComPath',
    'VirtualMachineRole', 'PodAdminState', 'PodCurrentState',

    'ReservationType', 'ReservationScope', 'InitConfig',

    'AccountPrivileges', 'AccountType', 'CommunityExtensionSlots', 'ContentAccessiblity',

    'PowerState', 'CloneStorageAllocation', 'CloneType', 'VirtualMachineLicenseType'
)
