from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class NFLRosterPosition(ModelEnum):
    BN = "BN"
    DEF = "DEF"
    FLEX = "FLEX"
    K = "K"
    QB = "QB"
    RB = "RB"
    SUPER_FLEX = "SUPER_FLEX"
    TE = "TE"
    WR = "WR"

    @classmethod
    def from_str(cls, s: str) -> NFLRosterPosition:
        if s.upper() == "BN":
            return NFLRosterPosition.BN
        elif s.upper() == "DEF":
            return NFLRosterPosition.DEF
        elif s.upper() == "FLEX":
            return NFLRosterPosition.FLEX
        elif s.upper() == "K":
            return NFLRosterPosition.K
        elif s.upper() == "QB":
            return NFLRosterPosition.QB
        elif s.upper() == "RB":
            return NFLRosterPosition.RB
        elif s.upper() == "SUPER_FLEX":
            return NFLRosterPosition.SUPER_FLEX
        elif s.upper() == "TE":
            return NFLRosterPosition.TE
        elif s.upper() == "WR":
            return NFLRosterPosition.WR
        else:
            cls._handle_unknown_value(NFLRosterPosition, s)
