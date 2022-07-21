from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.ModelEnum import ModelEnum
from sleeper.enum.PlayerStatus import PlayerStatus


@unique
class NFLPlayerStatus(PlayerStatus, ModelEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INJURED_RESERVE = "INJURED_RESERVE"
    NA = "NA"
    NON_FOOTBALL_INJURY = "NON_FOOTBALL_INJURY"
    PHYSICALLY_UNABLE_TO_PERFORM = "PHYSICALLY_UNABLE_TO_PERFORM"
    PRACTICE_SQUAD = "PRACTICE_SQUAD"

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
        elif s.upper() == "NON FOOTBALL INJURY":
            return NFLPlayerStatus.NON_FOOTBALL_INJURY
        elif s.upper() == "PHYSICALLY UNABLE TO PERFORM":
            return NFLPlayerStatus.PHYSICALLY_UNABLE_TO_PERFORM
        elif s.upper() == "PRACTICE SQUAD":
            return NFLPlayerStatus.PRACTICE_SQUAD
        else:
            cls._handle_unknown_value(NFLPlayerStatus, s)
