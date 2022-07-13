from dataclasses import dataclass
from typing import Optional

from sleeper.model.FromPlayoffMatchup import FromPlayoffMatchup


@dataclass(kw_only=True)
class PlayoffMatchup:
    round: int
    matchup_id: int
    team_1_roster_id: Optional[int]
    team_2_roster_id: Optional[int]
    winning_roster_id: Optional[int]
    losing_roster_id: Optional[int]
    team_1_from: Optional[FromPlayoffMatchup]
    team_2_from: Optional[FromPlayoffMatchup]
