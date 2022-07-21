from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class ScoringType(ModelEnum):
    DYNASTY = "DYNASTY"
    DYNASTY_PPR = "DYNASTY_PPR"
    DYNASTY_TWO_QB = "DYNASTY_2QB"
    HALF_PPR = "HALF_PPR"
    PPR = "PPR"
    STD = "STD"
    TWO_QB = "2QB"

    @classmethod
    def from_str(cls, s: str) -> ScoringType:
        if s.upper() == "DYNASTY":
            return ScoringType.DYNASTY
        elif s.upper() == "DYNASTY_PPR":
            return ScoringType.DYNASTY_PPR
        elif s.upper() == "DYNASTY_2QB":
            return ScoringType.DYNASTY_TWO_QB
        elif s.upper() == "HALF_PPR":
            return ScoringType.HALF_PPR
        elif s.upper() == "PPR":
            return ScoringType.PPR
        elif s.upper() == "STD":
            return ScoringType.STD
        elif s.upper() == "2QB":
            return ScoringType.TWO_QB
        else:
            cls._handle_unknown_value(ScoringType, s)
