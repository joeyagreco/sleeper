from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class TransactionType(ModelEnum):
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
            cls._handle_unknown_value(TransactionType, s)
