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

    @staticmethod
    def from_dict_list(faab_transaction_dict_list: dict) -> list[FAABTransaction]:
        faab_transactions = list()
        for faab_transaction_dict in faab_transaction_dict_list:
            faab_transactions.append(FAABTransaction.from_dict(faab_transaction_dict))
        return faab_transactions
