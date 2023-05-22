from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.DepthChart import DepthChart


@dataclass(kw_only=True)
class NFLDepthChart(DepthChart):
    C: list[str]
    FS: list[str]
    LCB: list[str]
    LDE: list[str]
    LG: list[str]
    LILB: list[str]
    LOLB: list[str]
    LT: list[str]
    NB: list[str]
    NT: list[str]
    PK: list[str]
    QB: list[str]
    RB: list[str]
    RCB: list[str]
    RDE: list[str]
    RG: list[str]
    RILB: list[str]
    ROLB: list[str]
    RT: list[str]
    SS: list[str]
    TE: list[str]
    WR1: list[str]
    WR2: list[str]
    WR3: list[str]

    @staticmethod
    def from_dict(nfl_depth_chart_dict: dict) -> NFLDepthChart:
        return NFLDepthChart(
            C=nfl_depth_chart_dict.get("C"),
            FS=nfl_depth_chart_dict.get("FS"),
            LCB=nfl_depth_chart_dict.get("LCB"),
            LDE=nfl_depth_chart_dict.get("LDE"),
            LG=nfl_depth_chart_dict.get("LG"),
            LILB=nfl_depth_chart_dict.get("LILB"),
            LOLB=nfl_depth_chart_dict.get("LOLB"),
            LT=nfl_depth_chart_dict.get("LT"),
            NB=nfl_depth_chart_dict.get("NB"),
            NT=nfl_depth_chart_dict.get("NT"),
            PK=nfl_depth_chart_dict.get("PK"),
            QB=nfl_depth_chart_dict.get("QB"),
            RB=nfl_depth_chart_dict.get("RB"),
            RCB=nfl_depth_chart_dict.get("RCB"),
            RDE=nfl_depth_chart_dict.get("RDE"),
            RG=nfl_depth_chart_dict.get("RG"),
            RILB=nfl_depth_chart_dict.get("RILB"),
            ROLB=nfl_depth_chart_dict.get("ROLB"),
            RT=nfl_depth_chart_dict.get("RT"),
            SS=nfl_depth_chart_dict.get("SS"),
            TE=nfl_depth_chart_dict.get("TE"),
            WR1=nfl_depth_chart_dict.get("WR1"),
            WR2=nfl_depth_chart_dict.get("WR2"),
            WR3=nfl_depth_chart_dict.get("WR3"),
        )
