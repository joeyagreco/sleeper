from __future__ import annotations

from abc import abstractmethod
from enum import Enum, unique

from sleeper.enum.Sport import Sport


@unique
class PlayerStatus(Enum):
    """
    Parent for all Enum statuses for each sport.
    """

    ...

    @classmethod
    @abstractmethod
    def from_str(cls, s: str) -> PlayerStatus:
        ...

    @staticmethod
    def enum(sport: Sport) -> PlayerStatus:
        from sleeper.enum.nfl.NFLPlayerStatus import NFLPlayerStatus

        if sport == Sport.NFL:
            return NFLPlayerStatus
        else:
            raise ValueError(f"Cannot find PlayerStatus for sport: '{sport.name}'.")
