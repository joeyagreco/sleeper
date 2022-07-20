from __future__ import annotations

from enum import unique, Enum


@unique
class PlayerStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INJURED_RESERVE = "INJURED_RESERVE"

    @classmethod
    def from_str(cls, s: str) -> PlayerStatus:
        if s.upper() == "ACTIVE":
            return PlayerStatus.ACTIVE
        elif s.upper() == "INACTIVE":
            return PlayerStatus.INACTIVE
        elif s.upper() == "INJURED_RESERVE":
            return PlayerStatus.INJURED_RESERVE
        else:
            raise ValueError(f"Invalid value for PlayerStatus: '{s}'.")
