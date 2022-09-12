from __future__ import annotations

from dataclasses import dataclass

from sleeper.model.Stats import Stats


@dataclass(kw_only=True)
class NFLStats(Stats):
    blk_kick: float
    blk_kick_ret_yd: float
    bonus_pass_cmp_25: float
    bonus_pass_yd_300: float
    bonus_pass_yd_400: float
    bonus_rec_rb: float
    bonus_rec_te: float
    bonus_rec_wr: float
    bonus_rec_yd_100: float
    bonus_rush_att_20: float
    bonus_rush_rec_yd_100: float
    bonus_sack_2p: float
    bonus_tkl_10p: float
    cmp_pct: float
    def_3_and_out: float
    def_4_and_stop: float
    def_forced_punts: float
    def_kr: float
    def_kr_lng: float
    def_kr_yd: float
    def_kr_ypa: float
    def_pass_def: float
    def_pr: float
    def_pr_lng: float
    def_pr_yd: float
    def_pr_ypa: float
    def_snp: float
    def_st_td: float
    def_st_tkl_solo: float
    fan_pts_allow: float
    fan_pts_allow_k: float
    fan_pts_allow_qb: float
    fan_pts_allow_rb: float
    fan_pts_allow_te: float
    fan_pts_allow_wr: float
    ff: float
    fga: float
    fgm: float
    fgm_20_29: float
    fgm_30_39: float
    fgm_40_49: float
    fgm_50p: float
    fgm_lng: float
    fgm_pct: float
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
    st_snp: float
    tm_def_snp: float
    tm_off_snp: float
    tm_st_snp: float

    @staticmethod
    def from_dict(nfl_stats_dict: dict) -> NFLStats:
        return NFLStats(blk_kick=nfl_stats_dict.get("blk_kick"),
                        blk_kick_ret_yd=nfl_stats_dict.get("blk_kick_ret_yd"),
                        bonus_pass_cmp_25=nfl_stats_dict.get("bonus_pass_cmp_25"),
                        bonus_pass_yd_300=nfl_stats_dict.get("bonus_pass_yd_300"),
                        bonus_pass_yd_400=nfl_stats_dict.get("bonus_pass_yd_400"),
                        bonus_rec_rb=nfl_stats_dict.get("bonus_rec_rb"),
                        bonus_rec_te=nfl_stats_dict.get("bonus_rec_te"),
                        bonus_rec_wr=nfl_stats_dict.get("bonus_rec_wr"),
                        bonus_rec_yd_100=nfl_stats_dict.get("bonus_rec_yd_100"),
                        bonus_rush_att_20=nfl_stats_dict.get("bonus_rush_att_20"),
                        bonus_rush_rec_yd_100=nfl_stats_dict.get("bonus_rush_rec_yd_100"),
                        bonus_sack_2p=nfl_stats_dict.get("bonus_sack_2p"),
                        bonus_tkl_10p=nfl_stats_dict.get("bonus_tkl_10p"),
                        cmp_pct=nfl_stats_dict.get("cmp_pct"),
                        def_3_and_out=nfl_stats_dict.get("def_3_and_out"),
                        def_4_and_stop=nfl_stats_dict.get("def_4_and_stop"),
                        def_forced_punts=nfl_stats_dict.get("def_forced_punts"),
                        def_kr=nfl_stats_dict.get("def_kr"),
                        def_kr_lng=nfl_stats_dict.get("def_kr_lng"),
                        def_kr_yd=nfl_stats_dict.get("def_kr_yd"),
                        def_kr_ypa=nfl_stats_dict.get("def_kr_ypa"),
                        def_pass_def=nfl_stats_dict.get("def_pass_def"),
                        def_pr=nfl_stats_dict.get("def_pr"),
                        def_pr_lng=nfl_stats_dict.get("def_pr_lng"),
                        def_pr_yd=nfl_stats_dict.get("def_pr_yd"),
                        def_pr_ypa=nfl_stats_dict.get("def_pr_ypa"),
                        def_snp=nfl_stats_dict.get("def_snp"),
                        def_st_td=nfl_stats_dict.get("def_st_td"),
                        def_st_tkl_solo=nfl_stats_dict.get("def_st_tkl_solo"),
                        fan_pts_allow=nfl_stats_dict.get("fan_pts_allow"),
                        fan_pts_allow_k=nfl_stats_dict.get("fan_pts_allow_k"),
                        fan_pts_allow_qb=nfl_stats_dict.get("fan_pts_allow_qb"),
                        fan_pts_allow_rb=nfl_stats_dict.get("fan_pts_allow_rb"),
                        fan_pts_allow_te=nfl_stats_dict.get("fan_pts_allow_te"),
                        fan_pts_allow_wr=nfl_stats_dict.get("fan_pts_allow_wr"),
                        ff=nfl_stats_dict.get("ff"),
                        fga=nfl_stats_dict.get("fga"),
                        fgm=nfl_stats_dict.get("fgm"),
                        fgm_20_29=nfl_stats_dict.get("fgm_20_29"),
                        fgm_30_39=nfl_stats_dict.get("fgm_30_39"),
                        fgm_40_49=nfl_stats_dict.get("fgm_40_49"),
                        fgm_50p=nfl_stats_dict.get("fgm_50p"),
                        fgm_lng=nfl_stats_dict.get("fgm_lng"),
                        fgm_pct=nfl_stats_dict.get("fgm_pct"),
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
                        st_snp=nfl_stats_dict.get("st_snp"),
                        tm_def_snp=nfl_stats_dict.get("tm_def_snp"),
                        tm_off_snp=nfl_stats_dict.get("tm_off_snp"),
                        tm_st_snp=nfl_stats_dict.get("tm_st_snp"))
