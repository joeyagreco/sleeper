from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.Sport import Sport
from sleeper.model.PlayerDraftPickMetadata import PlayerDraftPickMetadata


@dataclass(kw_only=True)
class PlayerDraftPick:
    draft_id: str
    draft_slot: int
    is_keeper: bool
    metadata: PlayerDraftPickMetadata
    pick_no: int
    picked_by: str
    player_id: str
    roster_id: str
    round: int

    @staticmethod
    def from_dict(player_draft_pick_dict: dict, sport: Sport) -> PlayerDraftPick:
        return PlayerDraftPick(
            player_id=player_draft_pick_dict.get("player_id"),
            picked_by=player_draft_pick_dict.get("picked_by"),
            roster_id=player_draft_pick_dict.get("roster_id"),
            round=player_draft_pick_dict.get("round"),
            draft_slot=player_draft_pick_dict.get("draft_slot"),
            pick_no=player_draft_pick_dict.get("pick_no"),
            metadata=PlayerDraftPickMetadata.from_dict(
                player_draft_pick_dict.get("metadata"), sport
            ),
            is_keeper=player_draft_pick_dict.get("is_keeper", False),
            draft_id=player_draft_pick_dict.get("draft_id"),
        )

    @staticmethod
    def from_dict_list(player_draft_pick_dict_list: list, sport: Sport) -> list[PlayerDraftPick]:
        player_draft_picks = list()
        for player_draft_pick in player_draft_pick_dict_list:
            player_draft_picks.append(PlayerDraftPick.from_dict(player_draft_pick, sport))
        return player_draft_picks
