from __future__ import annotations

from abc import abstractmethod
from enum import unique, Enum


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
