from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass

from sleeper.enum import Sport


@dataclass(kw_only=True)
class DepthChart:
    """
    Parent for all DepthChart models for each sport.
    """

    ...

    @staticmethod
    def model(sport: Sport) -> DepthChart:
        from sleeper.model.nfl.NFLDepthChart import NFLDepthChart

        if sport == Sport.NFL:
            return NFLDepthChart
        else:
            raise ValueError(f"Cannot find DepthChart for sport: '{sport.name}'.")

    @staticmethod
    @abstractmethod
    def from_dict(d: dict) -> DepthChart:
        ...
