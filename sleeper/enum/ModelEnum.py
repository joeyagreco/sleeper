from __future__ import annotations

from enum import Enum, unique


@unique
class ModelEnum(Enum):
    """
    Should be inherited by all model enums.
    """

    ...

    @staticmethod
    def _handle_unknown_value(enum_class: ModelEnum, value: str) -> None:
        print(f"Unknown value for {enum_class.__name__}: '{value}'.")
