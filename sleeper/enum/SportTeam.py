from __future__ import annotations

from abc import abstractmethod
from enum import unique, Enum


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
