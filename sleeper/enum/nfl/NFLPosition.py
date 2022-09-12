from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.ModelEnum import ModelEnum
from sleeper.enum.PlayerPosition import PlayerPosition


@unique
class NFLPosition(PlayerPosition, ModelEnum):
    C = "C"
    CB = "CB"
    DB = "DB"
    DE = "DE"
    DEF = "DEF"
    DL = "DL"
    DT = "DT"
    FB = "FB"
    FS = "FS"
    G = "G"
    ILB = "ILB"
    K = "K"
    LB = "LB"
    LEO = "LEO"
    LS = "LS"
    NA = "NA"
    NT = "NT"
    OG = "OG"
    OL = "OL"
    OLB = "OLB"
    OT = "OT"
    P = "P"
    QB = "QB"
    RB = "RB"
    S = "S"
    SS = "SS"
    T = "T"
    TE = "TE"
    TEAM = "TEAM"
    WR = "WR"

    @classmethod
    def from_str(cls, s: Optional[str]) -> NFLPosition:
        if s is None:
            return NFLPosition.NA
        elif s.upper() == "C":
            return NFLPosition.C
        elif s.upper() == "CB":
            return NFLPosition.CB
        elif s.upper() == "DB":
            return NFLPosition.DB
        elif s.upper() == "DE":
            return NFLPosition.DE
        elif s.upper() == "DEF":
            return NFLPosition.DEF
        elif s.upper() == "DL":
            return NFLPosition.DL
        elif s.upper() == "DT":
            return NFLPosition.DT
        elif s.upper() == "FB":
            return NFLPosition.FB
        elif s.upper() == "FS":
            return NFLPosition.FS
        elif s.upper() == "G":
            return NFLPosition.G
        elif s.upper() == "ILB":
            return NFLPosition.ILB
        elif s.upper() == "K":
            return NFLPosition.K
        elif s.upper() == "LB":
            return NFLPosition.LB
        elif s.upper() == "LEO":
            return NFLPosition.LEO
        elif s.upper() == "LS":
            return NFLPosition.LS
        elif s.upper() == "NT":
            return NFLPosition.NT
        elif s.upper() == "OG":
            return NFLPosition.OG
        elif s.upper() == "OL":
            return NFLPosition.OL
        elif s.upper() == "OLB":
            return NFLPosition.OLB
        elif s.upper() == "OT":
            return NFLPosition.OT
        elif s.upper() == "P":
            return NFLPosition.P
        elif s.upper() == "QB":
            return NFLPosition.QB
        elif s.upper() == "RB":
            return NFLPosition.RB
        elif s.upper() == "S":
            return NFLPosition.S
        elif s.upper() == "SS":
            return NFLPosition.SS
        elif s.upper() == "T":
            return NFLPosition.T
        elif s.upper() == "TE":
            return NFLPosition.TE
        elif s.upper() == "TEAM":
            return NFLPosition.TEAM
        elif s.upper() == "WR":
            return NFLPosition.WR
        else:
            cls._handle_unknown_value(NFLPosition, s)
