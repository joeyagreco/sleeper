from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class Matchup:
    starters: list[str]
    roster_id: int
    players: list[str]
    matchup_id: int
    points: float
    custom_points: Optional[float]
