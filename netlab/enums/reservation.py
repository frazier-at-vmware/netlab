from enum import Enum


class ReservationType(Enum):
    "Type of reservation."
    INDIVIDUAL = 'S'  # 'INDIVIDUAL'
    "Individual student reservation."
    ILT_CLASS = 'C'  # 'ILT_CLASS'
    "Instructor-led class reservation."
    TEAM = 'T'  # 'TEAM'
    "Team student reservation."
    INSTRUCTOR = 'I'  # 'INSTRUCTOR'
    "Instructor reservation for own use."


class ReservationScope(Enum):
    "Reservation scope."
    RELEVANT = 'RELEVANT'
    "Relevant to caller, i.e. reservations associated with you in context to user role."
    ALL = 'ALL'
    "All reservations."
    COMMUNITY = 'COMMUNITY'
    "Relevant to the community."
    CLASS = 'CLASS'
    "Relevant to your class."


class InitConfig(Enum):
    "Initial configuration."
    NONE = 'N'
    "No configs loaded."
    LAST = 'L'
    "Load last saved config (if any)."
    EXERCISE = 'E'
    "Load default for exercise (if any)."
