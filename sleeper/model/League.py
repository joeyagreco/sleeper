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
    total_rosters: int
    status: SeasonStatus
    sport: Sport
    settings: LeagueSettings
    season_type: SeasonType
    season: str
    scoring_settings: ScoringSettings
    roster_positions: list[RosterPosition]
    previous_league_id: str
    name: str
    league_id: str
    draft_id: str
    avatar: str

    @classmethod
    def from_dict(cls, league_dict: dict) -> League:
        return League(total_rosters=league_dict["total_rosters"],
                      status=SeasonStatus.from_str(league_dict["status"]),
                      sport=Sport.from_str(league_dict["sport"]),
                      settings=LeagueSettings.from_dict(league_dict["settings"]),
                      season_type=SeasonType.from_str(league_dict["season_type"]),
                      season=league_dict["season"],
                      scoring_settings=ScoringSettings.from_dict(league_dict["scoring_settings"]),
                      roster_positions=[RosterPosition.from_str(roster_position) for roster_position in
                                        league_dict["roster_positions"]],
                      previous_league_id=league_dict["previous_league_id"],
                      name=league_dict["name"],
                      league_id=league_dict["league_id"],
                      draft_id=league_dict["draft_id"],
                      avatar=league_dict["avatar"])
