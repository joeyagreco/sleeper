from __future__ import annotations

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

    @classmethod
    def from_dict(cls, roster_settings_dict: dict) -> RosterSettings:
        return RosterSettings(wins=roster_settings_dict["wins"],
                              waiver_position=roster_settings_dict["waiver_position"],
                              waiver_budget_used=roster_settings_dict["waiver_budget_used"],
                              total_moves=roster_settings_dict["total_moves"],
                              ties=roster_settings_dict["ties"],
                              losses=roster_settings_dict["losses"],
                              fpts_decimal=roster_settings_dict.get("fpts_decimal", None),
                              fpts_against_decimal=roster_settings_dict.get("fpts_against_decimal", None),
                              fpts_against=roster_settings_dict.get("fpts_against", None),
                              fpts=roster_settings_dict["fpts"])
