from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class RosterSettings:
    wins: int
    waiver_position: int
    waiver_budget_used: int
    total_moves: int
    ties: int
    losses: int
    fpts: int
    fpts_decimal: Optional[int]
    fpts_against: Optional[int]
    fpts_against_decimal: Optional[int]
