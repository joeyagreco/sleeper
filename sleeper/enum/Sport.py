from __future__ import annotations

from enum import unique, Enum


@unique
class Sport(Enum):
    NFL = "NFL"

    @classmethod
    def from_str(cls, s: str) -> Sport:
        if s.upper() == "NFL":
            return Sport.NFL
        else:
            raise ValueError(f"Invalid value for Sport: '{s}'.")
