from __future__ import annotations

from enum import unique, Enum


@unique
class TransactionType(Enum):
    FREE_AGENT = "FREE_AGENT"
    TRADE = "TRADE"
    WAIVER = "WAIVER"

    @classmethod
    def from_str(cls, s: str) -> TransactionType:
        if s.upper() == "FREE_AGENT":
            return TransactionType.FREE_AGENT
        elif s.upper() == "TRADE":
            return TransactionType.TRADE
        elif s.upper() == "WAIVER":
            return TransactionType.WAIVER
        else:
            raise ValueError(f"Invalid value for TransactionType: '{s}'.")
