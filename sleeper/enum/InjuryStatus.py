from __future__ import annotations

from enum import unique, Enum


@unique
class InjuryStatus(Enum):
    COV = "COV"
    NONE = "NONE"
    OUT = "OUT"
    PUP = "PUP"
    QUESTIONABLE = "QUESTIONABLE"

    @classmethod
    def from_str(cls, s: str) -> InjuryStatus:
        if s.upper() == "COV":
            return InjuryStatus.COV
        elif s.upper() == "":
            return InjuryStatus.NONE
        elif s.upper() == "OUT":
            return InjuryStatus.OUT
        elif s.upper() == "PUP":
            return InjuryStatus.PUP
        elif s.upper() == "QUESTIONABLE":
            return InjuryStatus.QUESTIONABLE
        else:
            raise ValueError(f"Invalid value for InjuryStatus: '{s}'.")
