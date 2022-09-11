from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class Company(ModelEnum):
    SPORTRADAR = "SPORTRADAR"

    @classmethod
    def from_str(cls, s: str) -> Company:
        if s.upper() == "SPORTRADAR":
            return Company.SPORTRADAR
        else:
            cls._handle_unknown_value(Company, s)
