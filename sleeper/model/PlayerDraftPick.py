from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.model.PlayerDraftPickMetadata import PlayerDraftPickMetadata


@dataclass(kw_only=True)
class PlayerDraftPick:
    player_id: Optional[str]
    picked_by: Optional[str]
    roster_id: Optional[str]
    round: Optional[int]
    draft_slot: Optional[int]
    pick_no: Optional[int]
    metadata: PlayerDraftPickMetadata
    is_keeper: bool
    draft_id: Optional[str]

    @staticmethod
    def from_dict(player_draft_pick_dict: dict) -> PlayerDraftPick:
        return PlayerDraftPick(player_id=player_draft_pick_dict.get("player_id", None),
                               picked_by=player_draft_pick_dict.get("picked_by", None),
                               roster_id=player_draft_pick_dict.get("roster_id", None),
                               round=player_draft_pick_dict.get("round", None),
                               draft_slot=player_draft_pick_dict.get("draft_slot", None),
                               pick_no=player_draft_pick_dict.get("pick_no", None),
                               metadata=PlayerDraftPickMetadata.from_dict(player_draft_pick_dict.get("metadata")),
                               is_keeper=player_draft_pick_dict.get("is_keeper", False),
                               draft_id=player_draft_pick_dict.get("draft_id", None))

    @staticmethod
    def from_dict_list(player_draft_pick_dict_list: dict) -> list[PlayerDraftPick]:
        player_draft_picks = list()
        for player_draft_pick in player_draft_pick_dict_list:
            player_draft_picks.append(PlayerDraftPick.from_dict(player_draft_pick))
        return player_draft_picks
