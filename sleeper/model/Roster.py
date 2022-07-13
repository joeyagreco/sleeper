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
