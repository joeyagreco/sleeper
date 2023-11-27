from __future__ import annotations

import datetime
from dataclasses import dataclass

from sleeper.enum import Sport, SportTeam
from sleeper.enum.SeasonStatus import SeasonStatus


@dataclass(kw_only=True)
class Game:
    away: SportTeam
    date: date
    game_id: str
    home: SportTeam
    status: SeasonStatus
    week: int

    @staticmethod
    def from_dict_list(game_dict_list: list, sport: Sport) -> list[Game]:
        game_list = list()
        for game_dict in game_dict_list:
            game_list.append(Game.from_dict(game_dict, sport))
        return game_list

    @staticmethod
    def from_dict(game_dict: dict, sport: Sport) -> Game:
        return Game(
            week=game_dict.get("week"),
            status=SeasonStatus.from_str(game_dict.get("status")),
            home=SportTeam.enum(sport).from_str(game_dict.get("home")),
            game_id=game_dict.get("game_id"),
            date=datetime.datetime.strptime(game_dict.get("date"), "%Y-%m-%d").date(),
            away=SportTeam.enum(sport).from_str(game_dict.get("away")),
        )
