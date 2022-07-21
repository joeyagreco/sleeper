from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.ModelEnum import ModelEnum


@unique
class PracticeParticipation(ModelEnum):
    NA = "NA"
    OUT = "OUT"

    @classmethod
    def from_str(cls, s: Optional[str]) -> PracticeParticipation:
        if s is None:
            return PracticeParticipation.NA
        elif s.upper() == "OUT":
            return PracticeParticipation.OUT
        else:
            cls._handle_unknown_value(PracticeParticipation, s)
