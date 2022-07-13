from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class FromPlayoffMatchup:
    won_matchup_id: Optional[int]
    lost_matchup_id: Optional[int]
