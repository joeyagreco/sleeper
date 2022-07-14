from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class FAABTransaction:
    sender: int
    receiver: int
    amount: int

    @staticmethod
    def from_dict(faab_transaction_dict: dict) -> FAABTransaction:
        return FAABTransaction(sender=faab_transaction_dict["sender"],
                               receiver=faab_transaction_dict["receiver"],
                               amount=faab_transaction_dict["amount"])
