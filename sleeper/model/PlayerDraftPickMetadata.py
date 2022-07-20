from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.NFLPlayerStatus import PlayerStatus
from sleeper.enum.PlayerPosition import PlayerPosition
from sleeper.enum.Sport import Sport
from sleeper.enum.SportTeam import SportTeam


@dataclass(kw_only=True)
class PlayerDraftPickMetadata:
    team: SportTeam
    status: PlayerStatus
    sport: Sport
    position: PlayerPosition
    player_id: Optional[str]
    number: Optional[str]
    news_updated: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    injury_status: InjuryStatus

    @staticmethod
    def from_dict(player_draft_pick_metadata_dict: dict) -> PlayerDraftPickMetadata:
        return PlayerDraftPickMetadata(team=SportTeam.from_str(player_draft_pick_metadata_dict.get("team")),
                                       status=PlayerStatus.from_str(player_draft_pick_metadata_dict.get("status")),
                                       sport=Sport.from_str(player_draft_pick_metadata_dict.get("sport")),
                                       position=PlayerPosition.from_str(
                                           player_draft_pick_metadata_dict.get("position")),
                                       player_id=player_draft_pick_metadata_dict.get("player_id", None),
                                       number=player_draft_pick_metadata_dict.get("number", None),
                                       news_updated=player_draft_pick_metadata_dict.get("news_updated", None),
                                       first_name=player_draft_pick_metadata_dict.get("first_name", None),
                                       last_name=player_draft_pick_metadata_dict.get("last_name", None),
                                       injury_status=InjuryStatus.from_str(
                                           player_draft_pick_metadata_dict.get("injury_status")))
