from __future__ import annotations

from enum import unique

from sleeper.enum.PlayerPosition import PlayerPosition


@unique
class NFLPosition(PlayerPosition):
    RB = "RB"

    @classmethod
    def from_str(cls, s: str) -> NFLPosition:
        if s.upper() == "RB":
            return NFLPosition.RB
        else:
            raise ValueError(f"Invalid value for NFLPosition: '{s}'.")
