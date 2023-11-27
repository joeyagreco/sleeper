from __future__ import annotations

from abc import abstractmethod
from enum import Enum, unique

from sleeper.enum.Sport import Sport


@unique
class SportTeam(Enum):
    """
    Parent for all Enum teams for each sport.
    """

    ...

    @classmethod
    @abstractmethod
    def from_str(cls, s: str) -> SportTeam:
        ...

    @staticmethod
    def enum(sport: Sport) -> SportTeam:
        from sleeper.enum.nfl.NFLTeam import NFLTeam

        if sport == Sport.NFL:
            return NFLTeam
        else:
            raise ValueError(f"Cannot find SportTeam for sport: '{sport.name}'.")
