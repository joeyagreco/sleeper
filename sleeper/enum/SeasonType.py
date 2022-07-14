from __future__ import annotations

from enum import unique, Enum


@unique
class SeasonType(Enum):
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
            raise ValueError(f"Invalid value for SeasonType: '{s}'.")
