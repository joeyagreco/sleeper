from __future__ import annotations

from enum import unique, Enum
from typing import Optional


@unique
class PracticeParticipation(Enum):
    NA = "NA"
    OUT = "OUT"

    @classmethod
    def from_str(cls, s: Optional[str]) -> PracticeParticipation:
        if s is None:
            return PracticeParticipation.NA
        elif s.upper() == "OUT":
            return PracticeParticipation.OUT
        else:
            raise ValueError(f"Invalid value for PracticeParticipation: '{s}'.")
