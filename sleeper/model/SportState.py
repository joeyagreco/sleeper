from __future__ import annotations

import datetime
from dataclasses import dataclass
from datetime import date

from sleeper.enum.SeasonType import SeasonType


@dataclass(kw_only=True)
class SportState:
    display_week: int
    league_create_season: str
    league_season: str
    leg: int
    previous_season: str
    season: str
    season_start_date: date
    season_type: SeasonType
    week: int

    @staticmethod
    def from_dict(sport_state_dict) -> SportState:
        season_start_date = (
            None
            if sport_state_dict.get("season_start_date") is None
            else datetime.datetime.strptime(
                sport_state_dict.get("season_start_date"), "%Y-%m-%d"
            ).date()
        )
        return SportState(
            week=sport_state_dict.get("week"),
            season_type=SeasonType.from_str(sport_state_dict.get("season_type")),
            season_start_date=season_start_date,
            season=sport_state_dict.get("season"),
            previous_season=sport_state_dict.get("previous_season"),
            leg=sport_state_dict.get("leg"),
            league_season=sport_state_dict.get("league_season"),
            league_create_season=sport_state_dict.get("league_create_season"),
            display_week=sport_state_dict.get("display_week"),
        )
