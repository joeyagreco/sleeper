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
