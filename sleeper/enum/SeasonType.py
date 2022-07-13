from __future__ import annotations

from enum import unique, Enum


@unique
class SeasonType(Enum):
    REGULAR = "REGULAR"

    @classmethod
    def from_str(cls, s: str) -> SeasonType:
        if s.upper() == "REGULAR":
            return SeasonType.REGULAR
        else:
            raise ValueError(f"Invalid value for SeasonType: '{s}'.")
