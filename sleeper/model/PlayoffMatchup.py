from __future__ import annotations

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

    @staticmethod
    def from_dict(playoff_matchup_object: dict) -> PlayoffMatchup:
        return PlayoffMatchup(round=playoff_matchup_object["r"],
                              matchup_id=playoff_matchup_object["m"],
                              team_1_roster_id=playoff_matchup_object["t1"],
                              team_2_roster_id=playoff_matchup_object["t2"],
                              winning_roster_id=playoff_matchup_object["w"],
                              losing_roster_id=playoff_matchup_object["l"],
                              team_1_from=FromPlayoffMatchup.from_dict(playoff_matchup_object.get("t1_from", None)),
                              team_2_from=FromPlayoffMatchup.from_dict(playoff_matchup_object.get("t2_from", None)))

    @staticmethod
    def from_dict_str(playoff_matchup_dict_list: dict) -> list[PlayoffMatchup]:
        playoff_matchups = list()
        for playoff_matchup_dict in playoff_matchup_dict_list:
            playoff_matchups.append(PlayoffMatchup.from_dict(playoff_matchup_dict))
        return playoff_matchups
