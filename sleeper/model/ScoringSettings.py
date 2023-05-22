from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class ScoringSettings:
    blk_kick: float
    blk_kick_ret_yd: float
    bonus_pass_yd_300: float
    bonus_pass_yd_400: float
    bonus_rec_yd_100: float
    bonus_rec_yd_200: float
    bonus_rush_yd_100: float
    bonus_rush_yd_200: float
    def_2pt: float
    def_pass_def: float
    def_st_ff: float
    def_st_fum_rec: float
    def_st_td: float
    def_td: float
    ff: float
    fg_ret_yd: float
    fgm: float
    fgm_0_19: float
    fgm_20_29: float
    fgm_30_39: float
    fgm_40_49: float
    fgm_50p: float
    fgmiss: float
    fgmiss_0_19: float
    fgmiss_20_29: float
    fgmiss_30_39: float
    fgmiss_40_49: float
    fgmiss_50p: float
    fum: float
    fum_lost: float
    fum_rec: float
    fum_ret_yd: float
    idp_blk_kick: float
    idp_def_td: float
    idp_ff: float
    idp_fum_rec: float
    idp_int: float
    idp_pass_def: float
    idp_sack: float
    idp_safe: float
    idp_tkl: float
    idp_tkl_ast: float
    idp_tkl_solo: float
    int: float
    int_ret_yd: float
    kr_td: float
    kr_yd: float
    pass_2pt: float
    pass_att: float
    pass_cmp: float
    pass_cmp_40p: float
    pass_inc: float
    pass_int: float
    pass_sack: float
    pass_td: float
    pass_yd: float
    pr_td: float
    pr_yd: float
    pts_allow_0: float
    pts_allow_14_20: float
    pts_allow_1_6: float
    pts_allow_21_27: float
    pts_allow_28_34: float
    pts_allow_35p: float
    pts_allow_7_13: float
    qb_hit: float
    rec: float
    rec_2pt: float
    rec_40p: float
    rec_td: float
    rec_yd: float
    rush_2pt: float
    rush_40p: float
    rush_att: float
    rush_td: float
    rush_yd: float
    sack: float
    sack_yd: float
    safe: float
    st_ff: float
    st_fum_rec: float
    st_td: float
    st_tkl_solo: float
    tkl: float
    tkl_ast: float
    tkl_loss: float
    tkl_solo: float
    xpm: float
    xpmiss: float
    yds_allow_0_100: float
    yds_allow_100_199: float
    yds_allow_200_299: float
    yds_allow_300_349: float
    yds_allow_350_399: float
    yds_allow_400_449: float
    yds_allow_450_499: float
    yds_allow_500_549: float
    yds_allow_550p: float

    @staticmethod
    def from_dict(scoring_settings_dict: dict) -> ScoringSettings:
        return ScoringSettings(
            yds_allow_0_100=scoring_settings_dict.get("yds_allow_0_100"),
            yds_allow_100_199=scoring_settings_dict.get("yds_allow_100_199"),
            yds_allow_200_299=scoring_settings_dict.get("yds_allow_200_299"),
            yds_allow_300_349=scoring_settings_dict.get("yds_allow_300_349"),
            yds_allow_350_399=scoring_settings_dict.get("yds_allow_350_399"),
            yds_allow_400_449=scoring_settings_dict.get("yds_allow_400_449"),
            yds_allow_450_499=scoring_settings_dict.get("yds_allow_450_499"),
            yds_allow_500_549=scoring_settings_dict.get("yds_allow_500_549"),
            yds_allow_550p=scoring_settings_dict.get("yds_allow_550p"),
            fgm=scoring_settings_dict.get("fgm"),
            fgm_0_19=scoring_settings_dict.get("fgm_0_19"),
            fgm_20_29=scoring_settings_dict.get("fgm_20_29"),
            fgm_30_39=scoring_settings_dict.get("fgm_30_39"),
            fgm_40_49=scoring_settings_dict.get("fgm_40_49"),
            fgm_50p=scoring_settings_dict.get("fgm_50p"),
            fgmiss=scoring_settings_dict.get("fgmiss"),
            fgmiss_0_19=scoring_settings_dict.get("fgmiss_0_19"),
            fgmiss_20_29=scoring_settings_dict.get("fgmiss_20_29"),
            fgmiss_30_39=scoring_settings_dict.get("fgmiss_30_39"),
            fgmiss_40_49=scoring_settings_dict.get("fgmiss_40_49"),
            fgmiss_50p=scoring_settings_dict.get("fgmiss_50p"),
            fg_ret_yd=scoring_settings_dict.get("fg_ret_yd"),
            pass_2pt=scoring_settings_dict.get("pass_2pt"),
            pass_int=scoring_settings_dict.get("pass_int"),
            pass_sack=scoring_settings_dict.get("pass_sack"),
            pass_cmp=scoring_settings_dict.get("pass_cmp"),
            pass_cmp_40p=scoring_settings_dict.get("pass_cmp_40p"),
            pass_inc=scoring_settings_dict.get("pass_inc"),
            pass_att=scoring_settings_dict.get("pass_att"),
            pass_yd=scoring_settings_dict.get("pass_yd"),
            pass_td=scoring_settings_dict.get("pass_td"),
            def_pass_def=scoring_settings_dict.get("def_pass_def"),
            def_td=scoring_settings_dict.get("def_td"),
            def_st_fum_rec=scoring_settings_dict.get("def_st_fum_rec"),
            def_st_td=scoring_settings_dict.get("def_st_td"),
            def_st_ff=scoring_settings_dict.get("def_st_ff"),
            def_2pt=scoring_settings_dict.get("def_2pt"),
            st_fum_rec=scoring_settings_dict.get("st_fum_rec"),
            st_ff=scoring_settings_dict.get("st_ff"),
            st_tkl_solo=scoring_settings_dict.get("st_tkl_solo"),
            st_td=scoring_settings_dict.get("st_td"),
            fum_rec=scoring_settings_dict.get("fum_rec"),
            fum_lost=scoring_settings_dict.get("fum_lost"),
            fum=scoring_settings_dict.get("fum"),
            fum_ret_yd=scoring_settings_dict.get("fum_ret_yd"),
            idp_safe=scoring_settings_dict.get("idp_safe"),
            idp_ff=scoring_settings_dict.get("idp_ff"),
            idp_blk_kick=scoring_settings_dict.get("idp_blk_kick"),
            idp_int=scoring_settings_dict.get("idp_int"),
            idp_tkl=scoring_settings_dict.get("idp_tkl"),
            idp_def_td=scoring_settings_dict.get("idp_def_td"),
            idp_pass_def=scoring_settings_dict.get("idp_pass_def"),
            idp_fum_rec=scoring_settings_dict.get("idp_fum_rec"),
            idp_sack=scoring_settings_dict.get("idp_sack"),
            idp_tkl_ast=scoring_settings_dict.get("idp_tkl_ast"),
            idp_tkl_solo=scoring_settings_dict.get("idp_tkl_solo"),
            rush_att=scoring_settings_dict.get("rush_att"),
            pts_allow_0=scoring_settings_dict.get("pts_allow_0"),
            pts_allow_1_6=scoring_settings_dict.get("pts_allow_1_6"),
            pts_allow_7_13=scoring_settings_dict.get("pts_allow_7_13"),
            pts_allow_14_20=scoring_settings_dict.get("pts_allow_14_20"),
            pts_allow_21_27=scoring_settings_dict.get("pts_allow_21_27"),
            pts_allow_28_34=scoring_settings_dict.get("pts_allow_28_34"),
            pts_allow_35p=scoring_settings_dict.get("pts_allow_35p"),
            rush_40p=scoring_settings_dict.get("rush_40p"),
            rush_2pt=scoring_settings_dict.get("rush_2pt"),
            rush_yd=scoring_settings_dict.get("rush_yd"),
            rush_td=scoring_settings_dict.get("rush_td"),
            bonus_rush_yd_100=scoring_settings_dict.get("bonus_rush_yd_100"),
            bonus_rush_yd_200=scoring_settings_dict.get("bonus_rush_yd_200"),
            bonus_rec_yd_100=scoring_settings_dict.get("bonus_rec_yd_100"),
            bonus_rec_yd_200=scoring_settings_dict.get("bonus_rec_yd_200"),
            bonus_pass_yd_300=scoring_settings_dict.get("bonus_pass_yd_300"),
            bonus_pass_yd_400=scoring_settings_dict.get("bonus_pass_yd_400"),
            rec_yd=scoring_settings_dict.get("rec_yd"),
            rec_2pt=scoring_settings_dict.get("rec_2pt"),
            rec=scoring_settings_dict.get("rec"),
            rec_td=scoring_settings_dict.get("rec_td"),
            rec_40p=scoring_settings_dict.get("rec_40p"),
            tkl=scoring_settings_dict.get("tkl"),
            tkl_loss=scoring_settings_dict.get("tkl_loss"),
            tkl_solo=scoring_settings_dict.get("tkl_solo"),
            tkl_ast=scoring_settings_dict.get("tkl_ast"),
            int_ret_yd=scoring_settings_dict.get("int_ret_yd"),
            int=scoring_settings_dict.get("int"),
            pr_td=scoring_settings_dict.get("pr_td"),
            pr_yd=scoring_settings_dict.get("pr_yd"),
            sack_yd=scoring_settings_dict.get("sack_yd"),
            sack=scoring_settings_dict.get("sack"),
            kr_yd=scoring_settings_dict.get("kr_yd"),
            kr_td=scoring_settings_dict.get("kr_td"),
            blk_kick=scoring_settings_dict.get("blk_kick"),
            blk_kick_ret_yd=scoring_settings_dict.get("blk_kick_ret_yd"),
            xpmiss=scoring_settings_dict.get("xpmiss"),
            ff=scoring_settings_dict.get("ff"),
            qb_hit=scoring_settings_dict.get("qb_hit"),
            xpm=scoring_settings_dict.get("xpm"),
            safe=scoring_settings_dict.get("safe"),
        )
