from __future__ import annotations

from enum import unique

from sleeper.enum.SportTeam import SportTeam


@unique
class NFLTeam(SportTeam):
    ARI = "ARI"
    GNB = "GNB"

    @classmethod
    def from_str(cls, s: str) -> NFLTeam:
        if s.upper() == "ARI":
            return NFLTeam.ARI
        elif s.upper() == "GNB":
            return NFLTeam.GNB
        else:
            raise ValueError(f"Invalid value for NFLTeam: '{s}'.")
