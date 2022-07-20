from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.RosterPosition import RosterPosition
from sleeper.enum.SeasonStatus import SeasonStatus
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.LeagueSettings import LeagueSettings
from sleeper.model.ScoringSettings import ScoringSettings


@dataclass(kw_only=True)
class League:
    avatar: str
    draft_id: str
    league_id: str
    name: str
    previous_league_id: str
    roster_positions: list[RosterPosition]
    scoring_settings: ScoringSettings
    season: str
    season_type: SeasonType
    settings: LeagueSettings
    sport: Sport
    status: SeasonStatus
    total_rosters: int

    @staticmethod
    def from_dict(league_dict: dict) -> League:
        return League(total_rosters=league_dict.get("total_rosters"),
                      status=SeasonStatus.from_str(league_dict.get("status")),
                      sport=Sport.from_str(league_dict.get("sport")),
                      settings=LeagueSettings.from_dict(league_dict.get("settings")),
                      season_type=SeasonType.from_str(league_dict.get("season_type")),
                      season=league_dict.get("season"),
                      scoring_settings=ScoringSettings.from_dict(league_dict.get("scoring_settings")),
                      roster_positions=[RosterPosition.from_str(roster_position) for roster_position in
                                        league_dict.get("roster_positions")],
                      previous_league_id=league_dict.get("previous_league_id"),
                      name=league_dict.get("name"),
                      league_id=league_dict.get("league_id"),
                      draft_id=league_dict.get("draft_id"),
                      avatar=league_dict.get("avatar"))

    @staticmethod
    def from_dict_list(league_dict_list: dict) -> list[League]:
        leagues = list()
        for league_dict in league_dict_list:
            leagues.append(League.from_dict(league_dict))
        return leagues
