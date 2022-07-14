from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class LeagueSettings:
    waiver_type: int
    waiver_day_of_week: int
    waiver_clear_days: int
    waiver_budget: int
    type: Optional[int]
    trade_review_days: int
    trade_deadline: int
    start_week: Optional[int]
    reserve_slots: Optional[int]
    reserve_allow_out: Optional[int]
    playoff_week_start: int
    playoff_teams: int
    pick_trading: Optional[int]
    offseason_adds: Optional[int]
    num_teams: int
    max_keepers: Optional[int]
    leg: int
    last_scored_leg: Optional[int]
    last_report: Optional[int]
    draft_rounds: Optional[int]
