from enum import Enum


class AccountPrivileges(Enum):
    ""
    COMWIDE = 'COMWIDE'
    "Community Administrator."
    SYSWIDE = 'SYSWIDE'
    "Systemwide Administrator."
    POD_DESIGNER = 'POD_DESIGNER'
    "Allows use of Pod Designer."
    LAB_DESIGNER = 'LAB_DESIGNER'
    "Allows use of Lab Designer."


class AccountType(Enum):
    """
    Account type.
    """
    STUDENT = 'S'
    "Student"
    INSTRUCTOR = 'I'
    "Instructor"
    ADMIN = 'Z'
    "Admin"


class CommunityExtensionSlots(Enum):
    "The number of times a reservation can be extended."
    UNLIMITED = -1
    "Allow unlimited extensions."
