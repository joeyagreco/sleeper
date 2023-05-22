from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class FromPlayoffMatchup:
    lost_matchup_id: int
    won_matchup_id: int

    @staticmethod
    def from_dict(from_playoff_matchup_object: Optional[dict]) -> Optional[FromPlayoffMatchup]:
        if from_playoff_matchup_object is None:
            return None
        return FromPlayoffMatchup(
            won_matchup_id=from_playoff_matchup_object.get("w"),
            lost_matchup_id=from_playoff_matchup_object.get("l"),
        )
