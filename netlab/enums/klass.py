from enum import Enum


class ClassLabLimit(Enum):
    """
    Lab limit settings.
    """
    ENFORCE = 'E'
    "Enforce class lab limit."
    INSTRUCTOR = 'I'
    "Instructor override."


class ClassEmailLogs(Enum):
    """
    Email reservation logs for real equipment pods.
    """
    NO = 'N'
    "Don't email logs."
    INSTRUCTOR = 'P'
    "Email to primary instructor."


class ClassExtensionSlots(Enum):
    """
    The number of times a reservation can be extended.
    """
    COMMUNITY = -1
    "Use the community setting."


class ContentAccessiblity(Enum):
    """
    Content accessiblity.
    """
    GLOBAL = 'G'
    "Globally accessible."
    PRIVATE = 'P'
    "Private."
