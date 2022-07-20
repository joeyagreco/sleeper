from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class LeagueSettings:
    draft_rounds: int
    last_report: int
    last_scored_leg: int
    leg: int
    max_keepers: int
    num_teams: int
    offseason_adds: int
    pick_trading: int
    playoff_teams: int
    playoff_week_start: int
    reserve_allow_out: int
    reserve_slots: int
    start_week: int
    trade_deadline: int
    trade_review_days: int
    type: int
    waiver_budget: int
    waiver_clear_days: int
    waiver_day_of_week: int
    waiver_type: int

    @staticmethod
    def from_dict(settings_dict: dict) -> LeagueSettings:
        return LeagueSettings(waiver_type=settings_dict.get("waiver_type"),
                              waiver_day_of_week=settings_dict.get("waiver_day_of_week"),
                              waiver_clear_days=settings_dict.get("waiver_clear_days"),
                              waiver_budget=settings_dict.get("waiver_budget"),
                              type=settings_dict.get("type"),
                              trade_review_days=settings_dict.get("trade_review_days"),
                              trade_deadline=settings_dict.get("trade_deadline"),
                              start_week=settings_dict.get("start_week"),
                              reserve_slots=settings_dict.get("reserve_slots"),
                              reserve_allow_out=settings_dict.get("reserve_allow_out"),
                              playoff_week_start=settings_dict.get("playoff_week_start"),
                              playoff_teams=settings_dict.get("playoff_teams"),
                              pick_trading=settings_dict.get("pick_trading"),
                              offseason_adds=settings_dict.get("offseason_adds"),
                              num_teams=settings_dict.get("num_teams"),
                              max_keepers=settings_dict.get("max_keepers"),
                              leg=settings_dict.get("leg"),
                              last_scored_leg=settings_dict.get("last_scored_leg"),
                              last_report=settings_dict.get("last_report"),
                              draft_rounds=settings_dict.get("draft_rounds"))
