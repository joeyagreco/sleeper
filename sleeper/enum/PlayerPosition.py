from __future__ import annotations

from abc import abstractmethod
from enum import unique, Enum


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
