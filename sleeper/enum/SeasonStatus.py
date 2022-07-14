from __future__ import annotations

from enum import unique, Enum


@unique
class SeasonStatus(Enum):
    COMPLETE = "COMPLETE"
    DRAFTING = "DRAFTING"
    IN_SEASON = "IN_SEASON"
    PRE_DRAFT = "PRE_DRAFT"

    @classmethod
    def from_str(cls, s: str) -> SeasonStatus:
        if s.upper() == "COMPLETE":
            return SeasonStatus.COMPLETE
        elif s.upper() == "DRAFTING":
            return SeasonStatus.DRAFTING
        elif s.upper() == "IN_SEASON":
            return SeasonStatus.IN_SEASON
        elif s.upper() == "PRE_DRAFT":
            return SeasonStatus.PRE_DRAFT
        else:
            raise ValueError(f"Invalid value for Status: '{s}'.")
