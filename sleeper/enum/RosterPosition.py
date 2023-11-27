from __future__ import annotations

from abc import abstractmethod
from enum import Enum, unique

from sleeper.enum.nfl.NFLRosterPosition import NFLRosterPosition
from sleeper.enum.Sport import Sport


@unique
class RosterPosition(Enum):
    """
    Parent for all Enum roster positions for each sport.
    """

    ...

    @classmethod
    @abstractmethod
    def from_str(cls, s: str) -> RosterPosition:
        ...

    @staticmethod
    def enum(sport: Sport) -> RosterPosition:
        if sport == Sport.NFL:
            return NFLRosterPosition
        else:
            raise ValueError(f"Cannot find RosterPosition for sport: '{sport.name}'.")
