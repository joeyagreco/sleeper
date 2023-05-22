from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.ScoringType import ScoringType


@dataclass(kw_only=True)
class DraftMetadata:
    description: str
    name: str
    scoring_type: ScoringType

    @staticmethod
    def from_dict(draft_metadata_dict: dict) -> DraftMetadata:
        return DraftMetadata(
            scoring_type=ScoringType.from_str(draft_metadata_dict.get("scoring_type")),
            name=draft_metadata_dict.get("name"),
            description=draft_metadata_dict.get("description"),
        )
