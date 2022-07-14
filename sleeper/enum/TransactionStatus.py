from __future__ import annotations

from enum import unique, Enum


@unique
class TransactionStatus(Enum):
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"

    @classmethod
    def from_str(cls, s: str) -> TransactionStatus:
        if s.upper() == "COMPLETE":
            return TransactionStatus.COMPLETE
        elif s.upper() == "FAILED":
            return TransactionStatus.FAILED
        else:
            raise ValueError(f"Invalid value for TransactionStatus: '{s}'.")
