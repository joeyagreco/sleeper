from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class Matchup:
    starters: list[str]
    roster_id: int
    players: list[str]
    matchup_id: int
    points: float
    custom_points: Optional[float]

    @staticmethod
    def from_dict(matchup_object_dict: dict) -> Matchup:
        return Matchup(starters=matchup_object_dict["starters"],
                       roster_id=matchup_object_dict["roster_id"],
                       players=matchup_object_dict["players"],
                       matchup_id=matchup_object_dict["matchup_id"],
                       points=matchup_object_dict["points"],
                       custom_points=matchup_object_dict["custom_points"])
    
    @staticmethod
    def from_dict_list(matchup_dict_list: dict) -> list[Matchup]:
        matchups = list()
        for matchup_dict in matchup_dict_list:
            matchups.append(Matchup.from_dict(matchup_dict))
        return matchups
