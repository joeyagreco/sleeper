from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class SeasonType(ModelEnum):
    OFF = "OFF"
    POST = "POST"
    PRE = "PRE"
    REGULAR = "REGULAR"

    @classmethod
    def from_str(cls, s: str) -> SeasonType:
        if s.upper() == "OFF":
            return SeasonType.OFF
        elif s.upper() == "POST":
            return SeasonType.POST
        elif s.upper() == "PRE":
            return SeasonType.PRE
        elif s.upper() == "REGULAR":
            return SeasonType.REGULAR
        else:
            cls._handle_unknown_value(SeasonType, s)
