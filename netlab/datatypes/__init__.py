"""
Additional Netlab datatypes.
"""

from .vm import VMAlloc, VMAllocTotal, VMAllocHostInfo

from .pod import PCCloneSpec

from .common import HDREvent, HDRResult

__all__ = (
    'VMAlloc', 'VMAllocTotal', 'VMAllocHostInfo',

    'PCCloneSpec',

    'HDREvent', 'HDRResult',
)
