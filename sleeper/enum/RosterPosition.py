from __future__ import annotations

from enum import unique, Enum


@unique
class RosterPosition(Enum):
    BN = "BN"
    DEF = "DEF"
    FLEX = "FLEX"
    K = "K"
    QB = "QB"
    RB = "RB"
    TE = "TE"
    WR = "WR"

    @classmethod
    def from_str(cls, s: str) -> RosterPosition:
        if s.upper() == "BN":
            return RosterPosition.BN
        elif s.upper() == "DEF":
            return RosterPosition.DEF
        elif s.upper() == "FLEX":
            return RosterPosition.FLEX
        elif s.upper() == "K":
            return RosterPosition.K
        elif s.upper() == "QB":
            return RosterPosition.QB
        elif s.upper() == "RB":
            return RosterPosition.RB
        elif s.upper() == "TE":
            return RosterPosition.TE
        elif s.upper() == "WR":
            return RosterPosition.WR
        else:
            raise ValueError(f"Invalid value for SeasonType: '{s}'.")
