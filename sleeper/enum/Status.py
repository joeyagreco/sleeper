from __future__ import annotations

from enum import unique, Enum


@unique
class Status(Enum):
    COMPLETE = "COMPLETE"
    DRAFTING = "DRAFTING"
    IN_SEASON = "IN_SEASON"
    PRE_DRAFT = "PRE_DRAFT"

    @classmethod
    def from_str(cls, s: str) -> Status:
        if s.upper() == "COMPLETE":
            return Status.COMPLETE
        elif s.upper() == "DRAFTING":
            return Status.DRAFTING
        elif s.upper() == "IN_SEASON":
            return Status.IN_SEASON
        elif s.upper() == "PRE_DRAFT":
            return Status.PRE_DRAFT
        else:
            raise ValueError(f"Invalid value for Status: '{s}'.")
