from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.ModelEnum import ModelEnum


@unique
class InjuryStatus(ModelEnum):
    COV = "COV"
    DNR = "DNR"
    DOUBTFUL = "DOUBTFUL"
    IR = "IR"
    NA = "NA"
    OUT = "OUT"
    PUP = "PUP"
    QUESTIONABLE = "QUESTIONABLE"
    SUS = "SUS"

    @classmethod
    def from_str(cls, s: Optional[str]) -> InjuryStatus:
        if s is None or s.upper() in ("NA", ""):
            return InjuryStatus.NA
        elif s.upper() == "COV":
            return InjuryStatus.COV
        elif s.upper() == "DOUBTFUL":
            return InjuryStatus.DOUBTFUL
        elif s.upper() == "DNR":
            return InjuryStatus.DNR
        elif s.upper() == "IR":
            return InjuryStatus.IR
        elif s.upper() == "OUT":
            return InjuryStatus.OUT
        elif s.upper() == "PUP":
            return InjuryStatus.PUP
        elif s.upper() == "QUESTIONABLE":
            return InjuryStatus.QUESTIONABLE
        elif s.upper() == "SUS":
            return InjuryStatus.SUS
        else:
            cls._handle_unknown_value(InjuryStatus, s)
