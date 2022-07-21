from __future__ import annotations

from enum import unique
from typing import Optional

from sleeper.enum.ModelEnum import ModelEnum
from sleeper.enum.SportTeam import SportTeam


@unique
class NFLTeam(SportTeam, ModelEnum):
    ARI = "ARI"
    ATL = "ATL"
    BAL = "BAL"
    BUF = "BUF"
    CAR = "CAR"
    CHI = "CHI"
    CIN = "CIN"
    CLE = "CLE"
    DAL = "DAL"
    DEN = "DEN"
    DET = "DET"
    GB = "GB"
    HOU = "HOU"
    IND = "IND"
    OAK = "OAK"
    JAX = "JAX"
    KC = "KC"
    LV = "LV"
    LAC = "LAC"
    LAR = "LAR"
    MIA = "MIA"
    MIN = "MIN"
    NA = "NA"
    NE = "NE"
    NO = "NO"
    NYG = "NYG"
    NYJ = "NYJ"
    PHI = "PHI"
    PIT = "PIT"
    SF = "SF"
    SEA = "SEA"
    TB = "TB"
    TEN = "TEN"
    WAS = "WAS"

    @classmethod
    def from_str(cls, s: Optional[str]) -> NFLTeam:
        if s is None:
            return NFLTeam.NA
        elif s.upper() == "ARI":
            return NFLTeam.ARI
        elif s.upper() == "ATL":
            return NFLTeam.ATL
        elif s.upper() == "BAL":
            return NFLTeam.BAL
        elif s.upper() == "BUF":
            return NFLTeam.BUF
        elif s.upper() == "CAR":
            return NFLTeam.CAR
        elif s.upper() == "CHI":
            return NFLTeam.CHI
        elif s.upper() == "CIN":
            return NFLTeam.CIN
        elif s.upper() == "CLE":
            return NFLTeam.CLE
        elif s.upper() == "DAL":
            return NFLTeam.DAL
        elif s.upper() == "DEN":
            return NFLTeam.DEN
        elif s.upper() == "DET":
            return NFLTeam.DET
        elif s.upper() == "GB":
            return NFLTeam.GB
        elif s.upper() == "HOU":
            return NFLTeam.HOU
        elif s.upper() == "IND":
            return NFLTeam.IND
        elif s.upper() == "JAX":
            return NFLTeam.JAX
        elif s.upper() == "KC":
            return NFLTeam.KC
        elif s.upper() == "LV":
            return NFLTeam.LV
        elif s.upper() == "LAC":
            return NFLTeam.LAC
        elif s.upper() == "LAR":
            return NFLTeam.LAR
        elif s.upper() == "MIA":
            return NFLTeam.MIA
        elif s.upper() == "MIN":
            return NFLTeam.MIN
        elif s.upper() == "NE":
            return NFLTeam.NE
        elif s.upper() == "NO":
            return NFLTeam.NO
        elif s.upper() == "NYG":
            return NFLTeam.NYG
        elif s.upper() == "NYJ":
            return NFLTeam.NYJ
        elif s.upper() == "OAK":
            return NFLTeam.OAK
        elif s.upper() == "PHI":
            return NFLTeam.PHI
        elif s.upper() == "PIT":
            return NFLTeam.PIT
        elif s.upper() == "SF":
            return NFLTeam.SF
        elif s.upper() == "SEA":
            return NFLTeam.SEA
        elif s.upper() == "TB":
            return NFLTeam.TB
        elif s.upper() == "TEN":
            return NFLTeam.TEN
        elif s.upper() == "WAS":
            return NFLTeam.WAS
        else:
            cls._handle_unknown_value(NFLTeam, s)
