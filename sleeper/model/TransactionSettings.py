from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class TransactionSettings:
    seq: Optional[int]
    waiver_bid: Optional[int]
