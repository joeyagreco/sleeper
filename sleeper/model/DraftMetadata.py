from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.enum.ScoringType import ScoringType


@dataclass(kw_only=True)
class DraftMetadata:
    scoring_type: ScoringType
    name: Optional[str]
    description: Optional[str]

    @staticmethod
    def from_dict(draft_metadata_dict: dict) -> DraftMetadata:
        return DraftMetadata(scoring_type=ScoringType.from_str(draft_metadata_dict["scoring_type"]),
                             name=draft_metadata_dict.get("name", None),
                             description=draft_metadata_dict.get("description", None))
