from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class PlayerTrend:
    count: int
    player_id: str

    @staticmethod
    def from_dict(player_trend_dict: dict) -> PlayerTrend:
        return PlayerTrend(
            player_id=player_trend_dict.get("player_id"), count=player_trend_dict.get("count")
        )

    @staticmethod
    def from_dict_list(player_trend_dict_list: list) -> list[PlayerTrend]:
        player_trends = list()
        for player_trend_dict in player_trend_dict_list:
            player_trends.append(PlayerTrend.from_dict(player_trend_dict))
        return player_trends
