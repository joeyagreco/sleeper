from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.Stats import Stats


@dataclass(kw_only=True)
class NFLStats(Stats):
    cmp_pct: float
    fum: float
    fum_lost: float
    gms_active: float
    gp: float
    gs: float
    off_snp: float
    pass_air_yd: float
    pass_att: float
    pass_cmp: float
    pass_fd: float
    pass_inc: float
    pass_lng: float
    pass_rtg: float
    pass_rz_att: float
    pass_sack: float
    pass_sack_yds: float
    pass_td: float
    pass_td_lng: float
    pass_yd: float
    pass_ypa: float
    pts_half_ppr: float
    pts_ppr: float
    pts_std: float
    rush_att: float
    rush_fd: float
    rush_lng: float
    rush_yac: float
    rush_yd: float
    rush_ypa: float
    tm_def_snp: float
    tm_off_snp: float
    tm_st_snp: float

    @staticmethod
    def from_dict(nfl_stats_dict: dict) -> NFLStats:
        return NFLStats(cmp_pct=nfl_stats_dict.get("cmp_pct"),
                        fum=nfl_stats_dict.get("fum"),
                        fum_lost=nfl_stats_dict.get("fum_lost"),
                        gms_active=nfl_stats_dict.get("gms_active"),
                        gp=nfl_stats_dict.get("gp"),
                        gs=nfl_stats_dict.get("gs"),
                        off_snp=nfl_stats_dict.get("off_snp"),
                        pass_air_yd=nfl_stats_dict.get("pass_air_yd"),
                        pass_att=nfl_stats_dict.get("pass_att"),
                        pass_cmp=nfl_stats_dict.get("pass_cmp"),
                        pass_fd=nfl_stats_dict.get("pass_fd"),
                        pass_inc=nfl_stats_dict.get("pass_inc"),
                        pass_lng=nfl_stats_dict.get("pass_lng"),
                        pass_rtg=nfl_stats_dict.get("pass_rtg"),
                        pass_rz_att=nfl_stats_dict.get("pass_rz_att"),
                        pass_sack=nfl_stats_dict.get("pass_sack"),
                        pass_sack_yds=nfl_stats_dict.get("pass_sack_yds"),
                        pass_td=nfl_stats_dict.get("pass_td"),
                        pass_td_lng=nfl_stats_dict.get("pass_td_lng"),
                        pass_yd=nfl_stats_dict.get("pass_yd"),
                        pass_ypa=nfl_stats_dict.get("pass_ypa"),
                        pts_half_ppr=nfl_stats_dict.get("pts_half_ppr"),
                        pts_ppr=nfl_stats_dict.get("pts_ppr"),
                        pts_std=nfl_stats_dict.get("pts_std"),
                        rush_att=nfl_stats_dict.get("rush_att"),
                        rush_fd=nfl_stats_dict.get("rush_fd"),
                        rush_lng=nfl_stats_dict.get("rush_lng"),
                        rush_yac=nfl_stats_dict.get("rush_yac"),
                        rush_yd=nfl_stats_dict.get("rush_yd"),
                        rush_ypa=nfl_stats_dict.get("rush_ypa"),
                        tm_def_snp=nfl_stats_dict.get("tm_def_snp"),
                        tm_off_snp=nfl_stats_dict.get("tm_off_snp"),
                        tm_st_snp=nfl_stats_dict.get("tm_st_snp"))
