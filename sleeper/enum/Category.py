from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class Category(ModelEnum):
    PROJ = "PROJ"
    STAT = "STAT"

    @classmethod
    def from_str(cls, s: str) -> Category:
        if s.upper() == "PROJ":
            return Category.PROJ
        elif s.upper() == "STAT":
            return Category.STAT
        else:
            cls._handle_unknown_value(Category, s)
