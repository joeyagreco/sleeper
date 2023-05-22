from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass

from sleeper.enum import Sport


@dataclass(kw_only=True)
class Stats:
    """
    Parent for all Stat models for each sport.
    """

    ...

    @staticmethod
    def model(sport: Sport) -> Stats:
        from sleeper.model.nfl.NFLStats import NFLStats

        if sport == Sport.NFL:
            return NFLStats
        else:
            raise ValueError(f"Cannot find Stats for sport: '{sport.name}'.")

    @staticmethod
    @abstractmethod
    def from_dict(d: dict) -> Stats:
        ...

    @abstractmethod
    def get_populated_stats(self) -> dict:
        ...
