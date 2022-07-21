from __future__ import annotations

from enum import unique, Enum


@unique
class ModelEnum(Enum):
    """
    Should be inherited by all model enums.
    """
    ...

    @staticmethod
    def _handle_unknown_value(enum_class: ModelEnum, value: str) -> None:
        # TODO: make this a logger warning
        print(f"Unknown value for {enum_class.__name__}: '{value}'.")
