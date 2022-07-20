from __future__ import annotations

from enum import unique, Enum


@unique
class TrendType(Enum):
    ADD = "ADD"
    DROP = "DROP"

    @classmethod
    def from_str(cls, s: str) -> TrendType:
        if s.upper() == "ADD":
            return TrendType.ADD
        elif s.upper() == "DROP":
            return TrendType.DROP
        else:
            raise ValueError(f"Invalid value for TrendType: '{s}'.")
