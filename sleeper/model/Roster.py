from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.RosterSettings import RosterSettings


@dataclass(kw_only=True)
class Roster:
    league_id: str
    owner_id: str
    players: list[str]
    reserve: list
    roster_id: int
    settings: RosterSettings
    starters: list[str]

    @staticmethod
    def from_dict(roster_dict: dict) -> Roster:
        return Roster(starters=roster_dict.get("starters"),
                      settings=RosterSettings.from_dict(roster_dict.get("settings")),
                      roster_id=roster_dict.get("roster_id"),
                      reserve=roster_dict.get("reserve"),
                      players=roster_dict.get("players"),
                      owner_id=roster_dict.get("owner_id"),
                      league_id=roster_dict.get("league_id"))

    @staticmethod
    def from_dict_list(roster_dict_list: dict) -> list[Roster]:
        rosters = list()
        for roster_dict in roster_dict_list:
            rosters.append(Roster.from_dict(roster_dict))
        return rosters
