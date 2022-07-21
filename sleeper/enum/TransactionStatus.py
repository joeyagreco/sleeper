from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class TransactionStatus(ModelEnum):
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"

    @classmethod
    def from_str(cls, s: str) -> TransactionStatus:
        if s.upper() == "COMPLETE":
            return TransactionStatus.COMPLETE
        elif s.upper() == "FAILED":
            return TransactionStatus.FAILED
        else:
            cls._handle_unknown_value(TransactionStatus, s)
