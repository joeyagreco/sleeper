from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.PlayerStatus import PlayerStatus


@unique
class NFLPlayerStatus(PlayerStatus):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INJURED_RESERVE = "INJURED_RESERVE"
    NA = "NA"
    PHYSICALLY_UNABLE_TO_PERFORM = "PHYSICALLY_UNABLE_TO_PERFORM"

    @classmethod
    def from_str(cls, s: Optional[str]) -> NFLPlayerStatus:
        if s is None:
            return NFLPlayerStatus.NA
        if s.upper() == "ACTIVE":
            return NFLPlayerStatus.ACTIVE
        elif s.upper() == "INACTIVE":
            return NFLPlayerStatus.INACTIVE
        elif s.upper() == "INJURED RESERVE":
            return NFLPlayerStatus.INJURED_RESERVE
        elif s.upper() == "PHYSICALLY UNABLE TO PERFORM":
            return NFLPlayerStatus.PHYSICALLY_UNABLE_TO_PERFORM
        else:
            raise ValueError(f"Invalid value for NFLPlayerStatus: '{s}'.")
