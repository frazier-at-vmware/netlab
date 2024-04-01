from enum import Enum


class HDRSeverity(Enum):
    """

    """
    NONE = 0
    "Show no warnings."
    FATAL = 1
    "Show FATAL warnings. Level 1."
    ERROR = 2
    "Show FATAL warnings. Level 2."
    WARN = 3
    "Show FATAL warnings. Level 3."
    SUCCESS = 4
    "Show FATAL warnings. Level 4."
    INFO = 5
    "Show FATAL warnings. Level 5."
    TRACE0 = 6
    "Show FATAL warnings. Level 6."
    TRACE1 = 7
    "Show FATAL warnings. Level 7."
    TRACE2 = 8
    "Show FATAL warnings. Level 8."


class HDRStatus(Enum):
    RUNNING = 0
    OK = 1
    FAILED = 2
    PARTIAL = 3
    CANCELLED = 4
    UNKNOWN = 9


class TimeFormat(Enum):
    ""
    HOUR24 = "24"
    "24 Hour"
    HOUR12 = "12"
    "12 Hour (am/pm)"


class DateFormat(Enum):
    ""
    ISO = 'ISO'
    "YYYY-MM-DD"
    DMY_SLASH = 'DMY_SLASH'
    "DD/MM/YYYY"
    DMY_HYPHEN = 'DMY_HYPHEN'
    "DD-MM-YYYY"
    DMY_DOT = 'DMY_DOT'
    "DD.MM.YYYY"
    DMY_SPACE = 'DMY_SPACE'
    "DD MM YYYY"
    DD_MMM_YYYY = 'DD_MMM_YYYY'
    "DD-Mon-YYYY"
    MDY_SLASH = 'MDY_SLASH'
    "MM/DD/YYYY"
    DAY_MDY = 'DAY_MDY'
    "Day Mon D, YYYY"
    CHINESE = 'CHINESE'
    "YYYY M D"
    JAPANESE = 'JAPANESE'
    "YYYY MM DD"
