from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class Sport(ModelEnum):
    LCS = "LCS"
    NBA = "NBA"
    NFL = "NFL"

    @classmethod
    def from_str(cls, s: str) -> Sport:
        if s.upper() == "LCS":
            return Sport.LCS
        elif s.upper() == "NBA":
            return Sport.NBA
        elif s.upper() == "NFL":
            return Sport.NFL
        else:
            cls._handle_unknown_value(Sport, s)
