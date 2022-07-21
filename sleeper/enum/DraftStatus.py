from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class DraftStatus(ModelEnum):
    COMPLETE = "COMPLETE"
    PRE_DRAFT = "PRE_DRAFT"

    @classmethod
    def from_str(cls, s: str) -> DraftStatus:
        if s.upper() == "COMPLETE":
            return DraftStatus.COMPLETE
        elif s.upper() == "PRE_DRAFT":
            return DraftStatus.PRE_DRAFT
        else:
            cls._handle_unknown_value(DraftStatus, s)
