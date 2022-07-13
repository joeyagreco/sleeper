from dataclasses import dataclass


@dataclass(kw_only=True)
class Settings:
    waiver_type: int
    waiver_day_of_week: int
    waiver_clear_days: int
    waiver_budget: int
    type: int
    trade_review_days: int
    trade_deadline: int
    start_week: int
    reserve_slots: int
    reserve_allow_out: int
    playoff_week_start: int
    playoff_teams: int
    pick_trading: int
    offseason_adds: int
    num_teams: int
    max_keepers: int
    leg: int
    last_scored_leg: int
    last_report: int
    draft_rounds: int
