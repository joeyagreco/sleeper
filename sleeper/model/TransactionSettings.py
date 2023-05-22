from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class TransactionSettings:
    seq: int
    waiver_bid: int

    @classmethod
    def from_dict(cls, transaction_settings_dict: Optional[dict]) -> Optional[TransactionSettings]:
        if transaction_settings_dict is None:
            return None
        return TransactionSettings(
            waiver_bid=transaction_settings_dict.get("waiver_bid"),
            seq=transaction_settings_dict.get("seq"),
        )
