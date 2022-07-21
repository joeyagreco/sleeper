from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class DraftType(ModelEnum):
    AUCTION = "AUCTION"
    LINEAR = "LINEAR"
    SNAKE = "SNAKE"

    @classmethod
    def from_str(cls, s: str) -> DraftType:
        if s.upper() == "AUCTION":
            return DraftType.AUCTION
        elif s.upper() == "LINEAR":
            return DraftType.LINEAR
        elif s.upper() == "SNAKE":
            return DraftType.SNAKE
        else:
            cls._handle_unknown_value(DraftType, s)
