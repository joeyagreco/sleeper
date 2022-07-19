from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class DraftSettings:
    teams: Optional[int]
    slots_wr: Optional[int]
    slots_te: Optional[int]
    slots_rb: Optional[int]
    slots_qb: Optional[int]
    slots_flex: Optional[int]
    slots_super_flex: Optional[int]
    slots_bn: Optional[int]
    rounds: Optional[int]
    pick_timer: Optional[int]
    reversal_round: Optional[int]
    player_type: Optional[int]
    nomination_timer: Optional[int]
    enforce_position_limits: Optional[int]
    cpu_autopick: Optional[int]
    alpha_sort: Optional[int]

    @staticmethod
    def from_dict(draft_settings_dict: dict) -> DraftSettings:
        return DraftSettings(teams=draft_settings_dict.get("teams", None),
                             slots_wr=draft_settings_dict.get("slots_wr", None),
                             slots_te=draft_settings_dict.get("slots_te", None),
                             slots_rb=draft_settings_dict.get("slots_rb", None),
                             slots_qb=draft_settings_dict.get("slots_qb", None),
                             slots_flex=draft_settings_dict.get("slots_flex", None),
                             slots_super_flex=draft_settings_dict.get("slots_super_flex", None),
                             slots_bn=draft_settings_dict.get("slots_bn", None),
                             rounds=draft_settings_dict.get("rounds", None),
                             pick_timer=draft_settings_dict.get("pick_timer", None),
                             reversal_round=draft_settings_dict.get("reversal_round", None),
                             player_type=draft_settings_dict.get("player_type", None),
                             nomination_timer=draft_settings_dict.get("nomination_timer", None),
                             enforce_position_limits=draft_settings_dict.get("enforce_position_limits", None),
                             cpu_autopick=draft_settings_dict.get("cpu_autopick", None),
                             alpha_sort=draft_settings_dict.get("alpha_sort", None))
