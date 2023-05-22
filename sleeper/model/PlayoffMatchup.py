from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.FromPlayoffMatchup import FromPlayoffMatchup


@dataclass(kw_only=True)
class PlayoffMatchup:
    losing_roster_id: int
    matchup_id: int
    round: int
    team_1_from: FromPlayoffMatchup
    team_1_roster_id: int
    team_2_from: FromPlayoffMatchup
    team_2_roster_id: int
    winning_roster_id: int
    p: int  # no documentation on what this field means

    @staticmethod
    def from_dict(playoff_matchup_object: dict) -> PlayoffMatchup:
        return PlayoffMatchup(
            round=playoff_matchup_object.get("r"),
            matchup_id=playoff_matchup_object.get("m"),
            team_1_roster_id=playoff_matchup_object.get("t1"),
            team_2_roster_id=playoff_matchup_object.get("t2"),
            winning_roster_id=playoff_matchup_object.get("w"),
            losing_roster_id=playoff_matchup_object.get("l"),
            team_1_from=FromPlayoffMatchup.from_dict(playoff_matchup_object.get("t1_from")),
            team_2_from=FromPlayoffMatchup.from_dict(playoff_matchup_object.get("t2_from")),
            p=playoff_matchup_object.get("p"),
        )

    @staticmethod
    def from_dict_str(playoff_matchup_dict_list: list) -> list[PlayoffMatchup]:
        playoff_matchups = list()
        for playoff_matchup_dict in playoff_matchup_dict_list:
            playoff_matchups.append(PlayoffMatchup.from_dict(playoff_matchup_dict))
        return playoff_matchups
