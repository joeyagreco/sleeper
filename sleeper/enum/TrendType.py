from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class TrendType(ModelEnum):
    ADD = "ADD"
    DROP = "DROP"

    @classmethod
    def from_str(cls, s: str) -> TrendType:
        if s.upper() == "ADD":
            return TrendType.ADD
        elif s.upper() == "DROP":
            return TrendType.DROP
        else:
            cls._handle_unknown_value(TrendType, s)
