from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class SeasonStatus(ModelEnum):
    COMPLETE = "COMPLETE"
    DRAFTING = "DRAFTING"
    IN_SEASON = "IN_SEASON"
    POSTPONED = "POSTPONED"
    POST_SEASON = "POST_SEASON"
    PRE_DRAFT = "PRE_DRAFT"

    @classmethod
    def from_str(cls, s: str) -> SeasonStatus:
        if s.upper() == "COMPLETE":
            return SeasonStatus.COMPLETE
        elif s.upper() == "DRAFTING":
            return SeasonStatus.DRAFTING
        elif s.upper() == "IN_SEASON":
            return SeasonStatus.IN_SEASON
        elif s.upper() == "POSTPONED":
            return SeasonStatus.POSTPONED
        elif s.upper() == "POST_SEASON":
            return SeasonStatus.POST_SEASON
        elif s.upper() == "PRE_DRAFT":
            return SeasonStatus.PRE_DRAFT
        else:
            cls._handle_unknown_value(SeasonStatus, s)
