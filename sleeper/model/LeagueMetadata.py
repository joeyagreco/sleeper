from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class LeagueMetadata:
    auto_continue: str
    # this pattern for divisions is weird
    # putting 8 to be safe/cover most (hopefully all) cases
    division_1: str
    division_1_avatar: str
    division_2: str
    division_2_avatar: str
    division_3: str
    division_3_avatar: str
    division_4: str
    division_4_avatar: str
    division_5: str
    division_5_avatar: str
    division_6: str
    division_6_avatar: str
    division_7: str
    division_7_avatar: str
    division_8: str
    division_8_avatar: str
    keeper_deadline: str
    latest_league_winner_roster_id: str

    @staticmethod
    def from_dict(metadata_dict: dict) -> LeagueMetadata:
        return LeagueMetadata(
            auto_continue=metadata_dict.get("auto_continue"),
            division_1=metadata_dict.get("division_1"),
            division_1_avatar=metadata_dict.get("division_1_avatar"),
            division_2=metadata_dict.get("division_2"),
            division_2_avatar=metadata_dict.get("division_2_avatar"),
            division_3=metadata_dict.get("division_3"),
            division_3_avatar=metadata_dict.get("division_3_avatar"),
            division_4=metadata_dict.get("division_4"),
            division_4_avatar=metadata_dict.get("division_4_avatar"),
            division_5=metadata_dict.get("division_5"),
            division_5_avatar=metadata_dict.get("division_5_avatar"),
            division_6=metadata_dict.get("division_6"),
            division_6_avatar=metadata_dict.get("division_6_avatar"),
            division_7=metadata_dict.get("division_7"),
            division_7_avatar=metadata_dict.get("division_7_avatar"),
            division_8=metadata_dict.get("division_8"),
            division_8_avatar=metadata_dict.get("division_8_avatar"),
            keeper_deadline=metadata_dict.get("keeper_deadline"),
            latest_league_winner_roster_id=metadata_dict.get("latest_league_winner_roster_id"),
        )
