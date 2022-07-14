from __future__ import annotations
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from sleeper.enum.SeasonType import SeasonType


@dataclass(kw_only=True)
class SportState:
    week: int
    season_type: SeasonType
    season_start_date: date
    season: str
    previous_season: str
    leg: int
    league_season: str
    league_create_season: str
    display_week: int

    @staticmethod
    def from_dict(sport_state_dict) -> SportState:
        return SportState(week=sport_state_dict["week"],
                          season_type=SeasonType.from_str(sport_state_dict["season_type"]),
                          season_start_date=sport_state_dict["season_start_date"],
                          season=sport_state_dict["season"],
                          previous_season=sport_state_dict["previous_season"],
                          leg=sport_state_dict["leg"],
                          league_season=sport_state_dict["league_season"],
                          league_create_season=sport_state_dict["league_create_season"],
                          display_week=sport_state_dict["display_week"])
