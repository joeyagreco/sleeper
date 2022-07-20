from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Matchup:
    custom_points: float
    matchup_id: int
    players: list[str]
    points: float
    roster_id: int
    starters: list[str]

    @staticmethod
    def from_dict(matchup_object_dict: dict) -> Matchup:
        return Matchup(starters=matchup_object_dict.get("starters"),
                       roster_id=matchup_object_dict.get("roster_id"),
                       players=matchup_object_dict.get("players"),
                       matchup_id=matchup_object_dict.get("matchup_id"),
                       points=matchup_object_dict.get("points"),
                       custom_points=matchup_object_dict.get("custom_points"))

    @staticmethod
    def from_dict_list(matchup_dict_list: dict) -> list[Matchup]:
        matchups = list()
        for matchup_dict in matchup_dict_list:
            matchups.append(Matchup.from_dict(matchup_dict))
        return matchups
