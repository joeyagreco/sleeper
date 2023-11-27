from __future__ import annotations

from abc import abstractmethod
from enum import Enum, unique

from sleeper.enum.Sport import Sport


@unique
class PlayerPosition(Enum):
    """
    Parent for all Enum positions for each sport.
    """

    ...

    @classmethod
    @abstractmethod
    def from_str(cls, s: str) -> PlayerPosition:
        ...

    @staticmethod
    def enum(sport: Sport) -> PlayerPosition:
        from sleeper.enum.nfl.NFLPosition import NFLPosition

        if sport == Sport.NFL:
            return NFLPosition
        else:
            raise ValueError(f"Cannot find PlayerPosition for sport: '{sport.name}'.")
