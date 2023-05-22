from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class DraftPick:
    draft_id: int
    owner_id: int
    previous_owner_id: int
    roster_id: int
    round: int
    season: str

    @staticmethod
    def from_dict(draft_pick_dict: dict) -> DraftPick:
        return DraftPick(
            season=draft_pick_dict.get("season"),
            round=draft_pick_dict.get("round"),
            roster_id=draft_pick_dict.get("roster_id"),
            previous_owner_id=draft_pick_dict.get("previous_owner_id"),
            owner_id=draft_pick_dict.get("owner_id"),
            draft_id=draft_pick_dict.get("draft_id"),
        )

    @classmethod
    def from_dict_list(cls, draft_pick_dict_list: list) -> list[DraftPick]:
        draft_picks = list()
        for draft_pick_dict in draft_pick_dict_list:
            draft_picks.append(DraftPick.from_dict(draft_pick_dict))
        return draft_picks
