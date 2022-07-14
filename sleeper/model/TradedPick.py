from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class TradedPick:
    season: Optional[str]
    round: Optional[int]
    roster_id: Optional[int]
    previous_owner_id: Optional[int]
    owner_id: Optional[int]
