from __future__ import annotations

import datetime
from dataclasses import dataclass
from datetime import date

from sleeper.enum import SportTeam, Sport, SeasonType
from sleeper.enum.Category import Category
from sleeper.enum.Company import Company
from sleeper.model.Stats import Stats


@dataclass(kw_only=True)
class PlayerStats:
    category: Category
    company: Company
    date: date
    game_id: str
    opponent: SportTeam
    player_id: str
    season: str
    season_type: SeasonType
    sport: Sport
    stats: Stats
    team: SportTeam
    week: int

    @staticmethod
    def from_dict(player_stats_dict: dict) -> PlayerStats:
        sport = Sport.from_str(player_stats_dict.get("sport"))
        date_ = None if player_stats_dict.get("date") is None else datetime.datetime.strptime(
            player_stats_dict.get("date"), "%Y-%m-%d").date()
        return PlayerStats(category=Category.from_str(player_stats_dict.get("category")),
                           company=Company.from_str(player_stats_dict.get("company")),
                           date=date_,
                           game_id=player_stats_dict.get("game_id"),
                           opponent=SportTeam.enum(sport).from_str(player_stats_dict.get("opponent")),
                           player_id=player_stats_dict.get("player_id"),
                           season=player_stats_dict.get("season"),
                           season_type=SeasonType.from_str(player_stats_dict.get("season_type")),
                           sport=sport,
                           stats=Stats.model(sport).from_dict(player_stats_dict.get("stats")),
                           team=SportTeam.enum(sport).from_str(player_stats_dict.get("team")),
                           week=player_stats_dict.get("week"))
