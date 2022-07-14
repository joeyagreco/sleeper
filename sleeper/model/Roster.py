from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.RosterSettings import RosterSettings


@dataclass(kw_only=True)
class Roster:
    starters: list[str]
    settings: RosterSettings
    roster_id: int
    reserve: list
    players: list[str]
    owner_id: str
    league_id: str

    @staticmethod
    def from_dict(roster_dict: dict) -> Roster:
        return Roster(starters=roster_dict["starters"],
                      settings=RosterSettings.from_dict(roster_dict["settings"]),
                      roster_id=roster_dict["roster_id"],
                      reserve=roster_dict["reserve"],
                      players=roster_dict["players"],
                      owner_id=roster_dict["owner_id"],
                      league_id=roster_dict["league_id"])
    
    @staticmethod
    def from_dict_list(roster_dict_list: dict) -> list[Roster]:
        rosters = list()
        for roster_dict in roster_dict_list:
            rosters.append(Roster.from_dict(roster_dict))
        return rosters
