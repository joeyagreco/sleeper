from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.DraftStatus import DraftStatus
from sleeper.enum.DraftType import DraftType
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.DraftMetadata import DraftMetadata
from sleeper.model.DraftSettings import DraftSettings


@dataclass(kw_only=True)
class Draft:
    created: int
    creators: list[str]
    draft_id: str
    draft_order: dict[str, int]
    last_message_id: str
    last_message_time: int
    last_picked: int
    league_id: str
    metadata: DraftMetadata
    season: str
    season_type: SeasonType
    settings: DraftSettings
    slot_to_roster_id: dict[str, int]
    sport: Sport
    start_time: int
    status: DraftStatus
    type: DraftType

    @staticmethod
    def from_dict(draft_dict: dict) -> Draft:
        return Draft(
            type=DraftType.from_str(draft_dict.get("type")),
            status=DraftStatus.from_str(draft_dict.get("status")),
            start_time=draft_dict.get("start_time"),
            sport=Sport.from_str(draft_dict.get("sport")),
            settings=DraftSettings.from_dict(draft_dict.get("settings")),
            season_type=SeasonType.from_str(draft_dict.get("season_type")),
            season=draft_dict.get("season"),
            metadata=DraftMetadata.from_dict(draft_dict.get("metadata")),
            league_id=draft_dict.get("league_id"),
            last_picked=draft_dict.get("last_picked"),
            last_message_time=draft_dict.get("last_message_time"),
            last_message_id=draft_dict.get("last_message_id"),
            draft_order=draft_dict.get("draft_order"),
            slot_to_roster_id=draft_dict.get("slot_to_roster_id"),
            draft_id=draft_dict.get("draft_id"),
            creators=draft_dict.get("creators"),
            created=draft_dict.get("created"),
        )

    @staticmethod
    def from_dict_list(draft_dict_list: list) -> list[Draft]:
        drafts = list()
        for draft_dict in draft_dict_list:
            drafts.append(Draft.from_dict(draft_dict))
        return drafts
