from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class Matchup:
    custom_points: Any  # not sure what this is
    matchup_id: int
    players: list[str]
    players_points: dict[str, float]
    points: float
    roster_id: int
    starters: list[str]
    starters_points: list[float]

    @staticmethod
    def from_dict(matchup_object_dict: dict) -> Matchup:
        return Matchup(
            starters=matchup_object_dict.get("starters"),
            roster_id=matchup_object_dict.get("roster_id"),
            players=matchup_object_dict.get("players"),
            matchup_id=matchup_object_dict.get("matchup_id"),
            points=matchup_object_dict.get("points"),
            custom_points=matchup_object_dict.get("custom_points"),
            players_points=matchup_object_dict.get("players_points"),
            starters_points=matchup_object_dict.get("starters_points"),
        )

    @staticmethod
    def from_dict_list(matchup_dict_list: list) -> list[Matchup]:
        matchups = list()
        for matchup_dict in matchup_dict_list:
            matchups.append(Matchup.from_dict(matchup_dict))
        return matchups
