from __future__ import annotations

from enum import unique, Enum


@unique
class DraftType(Enum):
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
            raise ValueError(f"Invalid value for DraftType: '{s}'.")
