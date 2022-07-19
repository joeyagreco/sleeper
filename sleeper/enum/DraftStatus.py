from __future__ import annotations

from enum import unique, Enum


@unique
class DraftStatus(Enum):
    COMPLETE = "COMPLETE"
    PRE_DRAFT = "PRE_DRAFT"

    @classmethod
    def from_str(cls, s: str) -> DraftStatus:
        if s.upper() == "COMPLETE":
            return DraftStatus.COMPLETE
        elif s.upper() == "PRE_DRAFT":
            return DraftStatus.PRE_DRAFT
        else:
            raise ValueError(f"Invalid value for DraftStatus: '{s}'.")
