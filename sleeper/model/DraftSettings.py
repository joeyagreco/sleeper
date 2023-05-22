from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class DraftSettings:
    alpha_sort: int
    cpu_autopick: int
    enforce_position_limits: int
    nomination_timer: int
    pick_timer: int
    player_type: int
    reversal_round: int
    rounds: int
    slots_bn: int
    slots_flex: int
    slots_qb: int
    slots_rb: int
    slots_super_flex: int
    slots_te: int
    slots_wr: int
    teams: int

    @staticmethod
    def from_dict(draft_settings_dict: dict) -> DraftSettings:
        return DraftSettings(
            teams=draft_settings_dict.get("teams"),
            slots_wr=draft_settings_dict.get("slots_wr"),
            slots_te=draft_settings_dict.get("slots_te"),
            slots_rb=draft_settings_dict.get("slots_rb"),
            slots_qb=draft_settings_dict.get("slots_qb"),
            slots_flex=draft_settings_dict.get("slots_flex"),
            slots_super_flex=draft_settings_dict.get("slots_super_flex"),
            slots_bn=draft_settings_dict.get("slots_bn"),
            rounds=draft_settings_dict.get("rounds"),
            pick_timer=draft_settings_dict.get("pick_timer"),
            reversal_round=draft_settings_dict.get("reversal_round"),
            player_type=draft_settings_dict.get("player_type"),
            nomination_timer=draft_settings_dict.get("nomination_timer"),
            enforce_position_limits=draft_settings_dict.get("enforce_position_limits"),
            cpu_autopick=draft_settings_dict.get("cpu_autopick"),
            alpha_sort=draft_settings_dict.get("alpha_sort"),
        )
