from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.PlayerPosition import PlayerPosition
from sleeper.enum.PlayerStatus import PlayerStatus
from sleeper.enum.Sport import Sport
from sleeper.enum.SportTeam import SportTeam


@dataclass(kw_only=True)
class PlayerDraftPickMetadata:
    first_name: str
    injury_status: InjuryStatus
    last_name: str
    news_updated: str
    number: str
    player_id: str
    position: PlayerPosition
    sport: Sport
    status: PlayerStatus
    team: SportTeam

    @staticmethod
    def from_dict(player_draft_pick_metadata_dict: dict, sport: Sport) -> PlayerDraftPickMetadata:
        return PlayerDraftPickMetadata(
            team=SportTeam.enum(sport).from_str(player_draft_pick_metadata_dict.get("team")),
            status=PlayerStatus.enum(sport).from_str(player_draft_pick_metadata_dict.get("status")),
            sport=Sport.from_str(player_draft_pick_metadata_dict.get("sport")),
            position=PlayerPosition.enum(sport).from_str(
                player_draft_pick_metadata_dict.get("position")
            ),
            player_id=player_draft_pick_metadata_dict.get("player_id"),
            number=player_draft_pick_metadata_dict.get("number"),
            news_updated=player_draft_pick_metadata_dict.get("news_updated"),
            first_name=player_draft_pick_metadata_dict.get("first_name"),
            last_name=player_draft_pick_metadata_dict.get("last_name"),
            injury_status=InjuryStatus.from_str(
                player_draft_pick_metadata_dict.get("injury_status")
            ),
        )
