from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.enum.TransactionStatus import TransactionStatus
from sleeper.enum.TransactionType import TransactionType
from sleeper.model.DraftPick import DraftPick
from sleeper.model.FAABTransaction import FAABTransaction
from sleeper.model.TransactionSettings import TransactionSettings


@dataclass(kw_only=True)
class Transaction:
    type: TransactionType
    transaction_id: str
    status_updated: int
    status: TransactionStatus
    settings: Optional[TransactionSettings]
    roster_ids: list[int]
    week: int
    adds: list[dict[str, int]]
    drops: list[dict[str, int]]
    draft_picks: list[DraftPick]
    creator: str
    created: int
    consenter_ids: list[int]
    waiver_budget: list[FAABTransaction]

    @staticmethod
    def from_dict(transaction_dict: dict) -> Transaction:
        return Transaction(type=TransactionType.from_str(transaction_dict["type"]),
                           transaction_id=transaction_dict["transaction_id"],
                           status_updated=transaction_dict["status_updated"],
                           status=TransactionStatus.from_str(transaction_dict["status"]),
                           settings=TransactionSettings.from_dict(transaction_dict["settings"]),
                           roster_ids=transaction_dict["roster_ids"],
                           week=transaction_dict["leg"],
                           adds=transaction_dict["adds"],
                           drops=transaction_dict["drops"],
                           draft_picks=DraftPick.from_dict_list(transaction_dict["draft_picks"]),
                           creator=transaction_dict["creator"],
                           created=transaction_dict["created"],
                           consenter_ids=transaction_dict["consenter_ids"],
                           waiver_budget=FAABTransaction.from_dict_list(transaction_dict["waiver_budget"]))

    @staticmethod
    def from_dict_list(transaction_dict_list: dict) -> list[Transaction]:
        transactions = list()
        for transaction_dict in transaction_dict_list:
            transactions.append(Transaction.from_dict(transaction_dict))
        return transactions
