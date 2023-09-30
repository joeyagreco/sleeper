from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.PlayoffRoundType import PlayoffRoundType


@dataclass(kw_only=True)
class LeagueSettings:
    bench_lock: int
    best_ball: int
    capacity_override: int
    commissioner_direct_invite: int
    daily_waivers: int
    daily_waivers_days: int
    daily_waivers_hour: int
    daily_waivers_last_ran: int
    disable_adds: int
    disable_trades: int
    divisions: int
    draft_rounds: int
    last_report: int
    last_scored_leg: int
    league_average_match: int
    leg: int
    max_keepers: int
    num_teams: int
    offseason_adds: int
    pick_trading: int
    playoff_round_type: int
    playoff_round_type_enum: PlayoffRoundType  # a more clear representation of the "playoff_round_type" field
    playoff_seed_type: int
    playoff_teams: int
    playoff_type: int
    playoff_week_start: int
    reserve_allow_cov: int
    reserve_allow_dnr: int
    reserve_allow_na: int
    reserve_allow_out: int
    reserve_allow_sus: int
    reserve_slots: int
    start_week: int
    taxi_allow_vets: int
    taxi_slots: int
    taxi_years: int
    trade_deadline: int
    trade_review_days: int
    type: int
    waiver_bid_min: int
    waiver_budget: int
    waiver_clear_days: int
    waiver_day_of_week: int
    waiver_type: int

    @staticmethod
    def from_dict(settings_dict: dict) -> LeagueSettings:
        # NOTE: it seems older sleeper leagues use "playoff_type" instead of "playoff_round_type".
        # if "playoff_round_type" is not present, we can use "playoff_type" to populate the enum.
        playff_round_type = settings_dict.get("playoff_round_type")
        playoff_type = settings_dict.get("playoff_type")
        raw_playoff_round_type = (
            playff_round_type if playff_round_type is not None else playoff_type
        )
        playoff_round_type_enum = PlayoffRoundType.from_int(raw_playoff_round_type)
        return LeagueSettings(
            waiver_type=settings_dict.get("waiver_type"),
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
            draft_rounds=settings_dict.get("draft_rounds"),
            bench_lock=settings_dict.get("bench_lock"),
            best_ball=settings_dict.get("best_ball"),
            capacity_override=settings_dict.get("capacity_override"),
            commissioner_direct_invite=settings_dict.get("commissioner_direct_invite"),
            daily_waivers=settings_dict.get("daily_waivers"),
            daily_waivers_days=settings_dict.get("daily_waivers_days"),
            daily_waivers_hour=settings_dict.get("daily_waivers_hour"),
            daily_waivers_last_ran=settings_dict.get("daily_waivers_last_ran"),
            disable_adds=settings_dict.get("disable_adds"),
            disable_trades=settings_dict.get("disable_trades"),
            divisions=settings_dict.get("divisions"),
            league_average_match=settings_dict.get("league_average_match"),
            playoff_round_type=playff_round_type,
            playoff_round_type_enum=playoff_round_type_enum,
            playoff_seed_type=settings_dict.get("playoff_seed_type"),
            playoff_type=playoff_type,
            reserve_allow_cov=settings_dict.get("reserve_allow_cov"),
            reserve_allow_dnr=settings_dict.get("reserve_allow_dnr"),
            reserve_allow_na=settings_dict.get("reserve_allow_na"),
            reserve_allow_sus=settings_dict.get("reserve_allow_sus"),
            taxi_allow_vets=settings_dict.get("taxi_allow_vets"),
            taxi_slots=settings_dict.get("taxi_slots"),
            taxi_years=settings_dict.get("taxi_years"),
            waiver_bid_min=settings_dict.get("waiver_bid_min"),
        )
