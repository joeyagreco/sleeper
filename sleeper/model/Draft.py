from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.enum.DraftStatus import DraftStatus
from sleeper.enum.DraftType import DraftType
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.DraftMetadata import DraftMetadata
from sleeper.model.DraftSettings import DraftSettings


@dataclass(kw_only=True)
class Draft:
    type: DraftType
    status: DraftStatus
    start_time: Optional[int]
    sport: Sport
    settings: DraftSettings
    season_type: SeasonType
    season: str
    metadata: DraftMetadata
    league_id: str
    last_picked: Optional[int]
    last_message_time: Optional[int]
    last_message_id: Optional[int]
    draft_order: dict[str, int]
    slot_to_roster_id: dict[str, int]
    draft_id: Optional[str]
    creators: None  # TODO
    created: Optional[int]

    @staticmethod
    def from_dict(draft_dict: dict) -> Draft:
        return Draft(type=DraftType.from_str(draft_dict["type"]),
                     status=DraftStatus.from_str(draft_dict["status"]),
                     start_time=draft_dict.get("start_time", None),
                     sport=Sport.from_str(draft_dict["sport"]),
                     settings=DraftSettings.from_dict(draft_dict["settings"]),
                     season_type=SeasonType.from_str(draft_dict["season_type"]),
                     season=draft_dict["season"],
                     metadata=DraftMetadata.from_dict(draft_dict["metadata"]),
                     league_id=draft_dict["league_id"],
                     last_picked=draft_dict.get("last_picked", None),
                     last_message_time=draft_dict.get("last_message_time", None),
                     last_message_id=draft_dict.get("last_message_id", None),
                     draft_order=draft_dict.get("draft_order", dict()),
                     slot_to_roster_id=draft_dict.get("slot_to_roster_id", dict()),
                     draft_id=draft_dict.get("draft_id", None),
                     creators=draft_dict.get("creators", None),
                     created=draft_dict.get("created", None))

    @staticmethod
    def from_dict_list(draft_dict_list: dict) -> list[Draft]:
        drafts = list()
        for draft_dict in draft_dict_list:
            drafts.append(Draft.from_dict(draft_dict))
        return drafts
