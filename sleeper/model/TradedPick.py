from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class TradedPick:
    season: Optional[str]
    round: Optional[int]
    roster_id: Optional[int]
    previous_owner_id: Optional[int]
    owner_id: Optional[int]

    @staticmethod
    def from_dict(traded_pick_dict: dict) -> TradedPick:
        return TradedPick(season=traded_pick_dict.get("season", None),
                          round=traded_pick_dict.get("round", None),
                          roster_id=traded_pick_dict.get("roster_id", None),
                          previous_owner_id=traded_pick_dict.get("previous_owner_id", None),
                          owner_id=traded_pick_dict.get("owner_id", None))

    @staticmethod
    def from_dict_list(traded_pick_dict_list: dict) -> list[TradedPick]:
        traded_picks = list()
        for traded_pick_dict in traded_pick_dict_list:
            traded_picks.append(TradedPick.from_dict(traded_pick_dict))
        return traded_picks
