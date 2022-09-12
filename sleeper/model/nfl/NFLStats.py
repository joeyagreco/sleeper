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
    fgm_yds: float
    fgm_yds_over_30: float
    fgmiss: float
    fgmiss_50p: float
    fum: float
    fum_lost: float
    fum_rec: float
    fum_ret_yd: float
    gms_active: float
    gp: float
    gs: float
    idp_blk_kick: float
    idp_ff: float
    idp_fum_rec: float
    idp_fum_ret_yd: float
    idp_int: float
    idp_int_ret_yd: float
    idp_pass_def: float
    idp_qb_hit: float
    idp_sack: float
    idp_sack_yd: float
    idp_tkl: float
    idp_tkl_ast: float
    idp_tkl_loss: float
    idp_tkl_solo: float
    int_: float
    int_ret_yd: float
    kr: float
    kr_lng: float
    kr_yd: float
    kr_ypa: float
    off_snp: float
    pass_air_yd: float
    pass_att: float
    pass_cmp: float
    pass_cmp_40p: float
    pass_fd: float
    pass_inc: float
    pass_int: float
    pass_lng: float
    pass_rtg: float
    pass_rz_att: float
    pass_sack: float
    pass_sack_yds: float
    pass_td: float
    pass_td_40p: float
    pass_td_50p: float
    pass_td_lng: float
    pass_yd: float
    pass_ypa: float
    penalty: float
    penalty_yd: float
    pr: float
    pr_lng: float
    pr_yd: float
    pr_ypa: float
    pts_allow: float
    pts_allow_14_20: float
    pts_allow_28_34: float
    pts_allow_35p: float
    pts_allow_7_13: float
    pts_half_ppr: float
    pts_ppr: float
    pts_std: float
    punt_in_20: float
    punt_net_yd: float
    punt_tb: float
    punt_yds: float
    punts: float
    qb_hit: float
    rec: float
    rec_0_4: float
    rec_10_19: float
    rec_20_29: float
    rec_30_39: float
    rec_40p: float
    rec_5_9: float
    rec_air_yd: float
    rec_drop: float
    rec_fd: float
    rec_lng: float
    rec_rz_tgt: float
    rec_td: float
    rec_td_40p: float
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
                        fgm_yds=nfl_stats_dict.get("fgm_yds"),
                        fgm_yds_over_30=nfl_stats_dict.get("fgm_yds_over_30"),
                        fgmiss=nfl_stats_dict.get("fgmiss"),
                        fgmiss_50p=nfl_stats_dict.get("fgmiss_50p"),
                        fum=nfl_stats_dict.get("fum"),
                        fum_lost=nfl_stats_dict.get("fum_lost"),
                        fum_rec=nfl_stats_dict.get("fum_rec"),
                        fum_ret_yd=nfl_stats_dict.get("fum_ret_yd"),
                        gms_active=nfl_stats_dict.get("gms_active"),
                        gp=nfl_stats_dict.get("gp"),
                        idp_blk_kick=nfl_stats_dict.get("idp_blk_kick"),
                        idp_ff=nfl_stats_dict.get("idp_ff"),
                        idp_fum_rec=nfl_stats_dict.get("idp_fum_rec"),
                        idp_fum_ret_yd=nfl_stats_dict.get("idp_fum_ret_yd"),
                        idp_int=nfl_stats_dict.get("idp_int"),
                        idp_int_ret_yd=nfl_stats_dict.get("idp_int_ret_yd"),
                        idp_pass_def=nfl_stats_dict.get("idp_pass_def"),
                        idp_qb_hit=nfl_stats_dict.get("idp_qb_hit"),
                        idp_sack=nfl_stats_dict.get("idp_sack"),
                        idp_sack_yd=nfl_stats_dict.get("idp_sack_yd"),
                        idp_tkl=nfl_stats_dict.get("idp_tkl"),
                        idp_tkl_ast=nfl_stats_dict.get("idp_tkl_ast"),
                        idp_tkl_loss=nfl_stats_dict.get("idp_tkl_loss"),
                        idp_tkl_solo=nfl_stats_dict.get("idp_tkl_solo"),
                        int_=nfl_stats_dict.get("int"),
                        int_ret_yd=nfl_stats_dict.get("int_ret_yd"),
                        kr=nfl_stats_dict.get("kr"),
                        kr_lng=nfl_stats_dict.get("kr_lng"),
                        kr_yd=nfl_stats_dict.get("kr_yd"),
                        kr_ypa=nfl_stats_dict.get("kr_ypa"),
                        gs=nfl_stats_dict.get("gs"),
                        off_snp=nfl_stats_dict.get("off_snp"),
                        pass_air_yd=nfl_stats_dict.get("pass_air_yd"),
                        pass_att=nfl_stats_dict.get("pass_att"),
                        pass_cmp=nfl_stats_dict.get("pass_cmp"),
                        pass_cmp_40p=nfl_stats_dict.get("pass_cmp_40p"),
                        pass_fd=nfl_stats_dict.get("pass_fd"),
                        pass_inc=nfl_stats_dict.get("pass_inc"),
                        pass_int=nfl_stats_dict.get("pass_int"),
                        pass_lng=nfl_stats_dict.get("pass_lng"),
                        pass_rtg=nfl_stats_dict.get("pass_rtg"),
                        pass_rz_att=nfl_stats_dict.get("pass_rz_att"),
                        pass_sack=nfl_stats_dict.get("pass_sack"),
                        pass_sack_yds=nfl_stats_dict.get("pass_sack_yds"),
                        pass_td=nfl_stats_dict.get("pass_td"),
                        pass_td_40p=nfl_stats_dict.get("pass_td_40p"),
                        pass_td_50p=nfl_stats_dict.get("pass_td_50p"),
                        pass_td_lng=nfl_stats_dict.get("pass_td_lng"),
                        pass_yd=nfl_stats_dict.get("pass_yd"),
                        pass_ypa=nfl_stats_dict.get("pass_ypa"),
                        penalty=nfl_stats_dict.get("penalty"),
                        penalty_yd=nfl_stats_dict.get("penalty_yd"),
                        pr=nfl_stats_dict.get("pr"),
                        pr_lng=nfl_stats_dict.get("pr_lng"),
                        pr_yd=nfl_stats_dict.get("pr_yd"),
                        pr_ypa=nfl_stats_dict.get("pr_ypa"),
                        pts_allow=nfl_stats_dict.get("pts_allow"),
                        pts_allow_14_20=nfl_stats_dict.get("pts_allow_14_20"),
                        pts_allow_28_34=nfl_stats_dict.get("pts_allow_28_34"),
                        pts_allow_35p=nfl_stats_dict.get("pts_allow_35p"),
                        pts_allow_7_13=nfl_stats_dict.get("pts_allow_7_13"),
                        pts_half_ppr=nfl_stats_dict.get("pts_half_ppr"),
                        pts_ppr=nfl_stats_dict.get("pts_ppr"),
                        pts_std=nfl_stats_dict.get("pts_std"),
                        punt_in_20=nfl_stats_dict.get("punt_in_20"),
                        punt_net_yd=nfl_stats_dict.get("punt_net_yd"),
                        punt_tb=nfl_stats_dict.get("punt_tb"),
                        punt_yds=nfl_stats_dict.get("punt_yds"),
                        punts=nfl_stats_dict.get("punts"),
                        qb_hit=nfl_stats_dict.get("qb_hit"),
                        rec=nfl_stats_dict.get("rec"),
                        rec_0_4=nfl_stats_dict.get("rec_0_4"),
                        rec_10_19=nfl_stats_dict.get("rec_10_19"),
                        rec_20_29=nfl_stats_dict.get("rec_20_29"),
                        rec_30_39=nfl_stats_dict.get("rec_30_39"),
                        rec_40p=nfl_stats_dict.get("rec_40p"),
                        rec_5_9=nfl_stats_dict.get("rec_5_9"),
                        rec_air_yd=nfl_stats_dict.get("rec_air_yd"),
                        rec_drop=nfl_stats_dict.get("rec_drop"),
                        rec_fd=nfl_stats_dict.get("rec_fd"),
                        rec_lng=nfl_stats_dict.get("rec_lng"),
                        rec_rz_tgt=nfl_stats_dict.get("rec_rz_tgt"),
                        rec_td=nfl_stats_dict.get("rec_td"),
                        rec_td_40p=nfl_stats_dict.get("rec_td_40p"),
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
