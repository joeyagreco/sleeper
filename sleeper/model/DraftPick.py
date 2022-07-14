from dataclasses import dataclass


@dataclass(kw_only=True)
class DraftPick:
    season: str
    round: int
    roster_id: int
    previous_owner_id: int
    owner_id: int
