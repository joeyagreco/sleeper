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
