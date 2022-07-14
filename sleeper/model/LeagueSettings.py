from __future__ import annotations

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

    @staticmethod
    def from_dict(settings_dict: dict) -> LeagueSettings:
        return LeagueSettings(waiver_type=settings_dict["waiver_type"],
                              waiver_day_of_week=settings_dict["waiver_day_of_week"],
                              waiver_clear_days=settings_dict["waiver_clear_days"],
                              waiver_budget=settings_dict["waiver_budget"],
                              type=settings_dict.get("type", None),
                              trade_review_days=settings_dict["trade_review_days"],
                              trade_deadline=settings_dict["trade_deadline"],
                              start_week=settings_dict.get("start_week", None),
                              reserve_slots=settings_dict.get("reserve_slots", None),
                              reserve_allow_out=settings_dict.get("reserve_allow_out", None),
                              playoff_week_start=settings_dict["playoff_week_start"],
                              playoff_teams=settings_dict["playoff_teams"],
                              pick_trading=settings_dict.get("pick_trading", None),
                              offseason_adds=settings_dict.get("offseason_adds", None),
                              num_teams=settings_dict["num_teams"],
                              max_keepers=settings_dict.get("max_keepers", None),
                              leg=settings_dict["leg"],
                              last_scored_leg=settings_dict.get("last_scored_leg", None),
                              last_report=settings_dict.get("last_report", None),
                              draft_rounds=settings_dict.get("draft_rounds"))
