from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sleeper.model.RosterSettings import RosterSettings


@dataclass(kw_only=True)
class Roster:
    co_owners: Any  # not sure what this is
    league_id: str
    metadata: dict[str, Any]  # not sure what this is
    owner_id: str
    players: list[str]
    player_map: Any  # not sure what this is
    reserve: list
    roster_id: int
    settings: RosterSettings
    starters: list[str]
    taxi: Any  # not sure what this is

    @staticmethod
    def from_dict(roster_dict: dict) -> Roster:
        return Roster(
            starters=roster_dict.get("starters"),
            settings=RosterSettings.from_dict(roster_dict.get("settings")),
            roster_id=roster_dict.get("roster_id"),
            reserve=roster_dict.get("reserve"),
            players=roster_dict.get("players"),
            owner_id=roster_dict.get("owner_id"),
            league_id=roster_dict.get("league_id"),
            co_owners=roster_dict.get("co_owners"),
            metadata=roster_dict.get("metadata"),
            player_map=roster_dict.get("player_map"),
            taxi=roster_dict.get("taxi"),
        )

    @staticmethod
    def from_dict_list(roster_dict_list: list) -> list[Roster]:
        rosters = list()
        for roster_dict in roster_dict_list:
            rosters.append(Roster.from_dict(roster_dict))
        return rosters
