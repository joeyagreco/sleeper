from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class TradedPick:
    owner_id: int
    previous_owner_id: int
    roster_id: int
    round: int
    season: str

    @staticmethod
    def from_dict(traded_pick_dict: dict) -> TradedPick:
        return TradedPick(
            season=traded_pick_dict.get("season"),
            round=traded_pick_dict.get("round"),
            roster_id=traded_pick_dict.get("roster_id"),
            previous_owner_id=traded_pick_dict.get("previous_owner_id"),
            owner_id=traded_pick_dict.get("owner_id"),
        )

    @staticmethod
    def from_dict_list(traded_pick_dict_list: list) -> list[TradedPick]:
        traded_picks = list()
        for traded_pick_dict in traded_pick_dict_list:
            traded_picks.append(TradedPick.from_dict(traded_pick_dict))
        return traded_picks
