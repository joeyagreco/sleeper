from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class ScoringSettings:
    yds_allow_0_100: Optional[float]
    yds_allow_100_199: Optional[float]
    yds_allow_200_299: Optional[float]
    yds_allow_300_349: Optional[float]
    yds_allow_350_399: Optional[float]
    yds_allow_400_449: Optional[float]
    yds_allow_450_499: Optional[float]
    yds_allow_500_549: Optional[float]
    yds_allow_550p: Optional[float]
    fgm: Optional[float]
    fgm_0_19: float
    fgm_20_29: float
    fgm_30_39: float
    fgm_40_49: float
    fgm_50p: float
    fgmiss: float
    fgmiss_0_19: Optional[float]
    fgmiss_20_29: Optional[float]
    fgmiss_30_39: Optional[float]
    fgmiss_40_49: Optional[float]
    fgmiss_50p: Optional[float]
    fg_ret_yd: Optional[float]
    pass_2pt: float
    pass_int: float
    pass_sack: Optional[float]
    pass_cmp: Optional[float]
    pass_cmp_40p: Optional[float]
    pass_inc: Optional[float]
    pass_att: Optional[float]
    pass_yd: float
    pass_td: float
    def_pass_def: Optional[float]
    def_td: float
    def_st_fum_rec: Optional[float]
    def_st_td: Optional[float]
    def_st_ff: Optional[float]
    def_2pt: Optional[float]
    st_fum_rec: float
    st_ff: float
    st_tkl_solo: Optional[float]
    st_td: float
    fum_rec: float
    fum_lost: float
    fum: float
    fum_ret_yd: Optional[float]
    idp_safe: Optional[float]
    idp_ff: Optional[float]
    idp_blk_kick: Optional[float]
    idp_int: Optional[float]
    idp_tkl: Optional[float]
    idp_def_td: Optional[float]
    idp_pass_def: Optional[float]
    idp_fum_rec: Optional[float]
    idp_sack: Optional[float]
    idp_tkl_ast: Optional[float]
    idp_tkl_solo: Optional[float]
    rush_att: Optional[float]
    pts_allow_0: float
    pts_allow_1_6: float
    pts_allow_7_13: float
    pts_allow_14_20: float
    pts_allow_21_27: float
    pts_allow_28_34: float
    pts_allow_35p: float
    rush_40p: Optional[float]
    rush_2pt: float
    rush_yd: float
    rush_td: float
    bonus_rush_yd_100: Optional[float]
    bonus_rush_yd_200: Optional[float]
    bonus_rec_yd_100: Optional[float]
    bonus_rec_yd_200: Optional[float]
    bonus_pass_yd_300: Optional[float]
    bonus_pass_yd_400: Optional[float]
    rec_yd: float
    rec_2pt: float
    rec: float
    rec_td: float
    rec_40p: Optional[float]
    tkl: Optional[float]
    tkl_loss: Optional[float]
    tkl_solo: Optional[float]
    tkl_ast: Optional[float]
    int_ret_yd: Optional[float]
    int: float
    pr_td: Optional[float]
    pr_yd: Optional[float]
    sack_yd: Optional[float]
    sack: float
    kr_yd: Optional[float]
    kr_td: Optional[float]
    blk_kick: float
    blk_kick_ret_yd: Optional[float]
    xpmiss: Optional[float]
    ff: float
    qb_hit: Optional[float]
    xpm: float
    safe: float

    @staticmethod
    def from_dict(scoring_settings_dict: dict) -> ScoringSettings:
        return ScoringSettings(yds_allow_0_100=scoring_settings_dict.get("yds_allow_0_100", None),
                               yds_allow_100_199=scoring_settings_dict.get("yds_allow_100_199", None),
                               yds_allow_200_299=scoring_settings_dict.get("yds_allow_200_299", None),
                               yds_allow_300_349=scoring_settings_dict.get("yds_allow_300_349", None),
                               yds_allow_350_399=scoring_settings_dict.get("yds_allow_350_399", None),
                               yds_allow_400_449=scoring_settings_dict.get("yds_allow_400_449", None),
                               yds_allow_450_499=scoring_settings_dict.get("yds_allow_450_499", None),
                               yds_allow_500_549=scoring_settings_dict.get("yds_allow_500_549", None),
                               yds_allow_550p=scoring_settings_dict.get("yds_allow_550p", None),
                               fgm=scoring_settings_dict.get("fgm", None),
                               fgm_0_19=scoring_settings_dict["fgm_0_19"],
                               fgm_20_29=scoring_settings_dict["fgm_20_29"],
                               fgm_30_39=scoring_settings_dict["fgm_30_39"],
                               fgm_40_49=scoring_settings_dict["fgm_40_49"],
                               fgm_50p=scoring_settings_dict["fgm_50p"],
                               fgmiss=scoring_settings_dict["fgmiss"],
                               fgmiss_0_19=scoring_settings_dict.get("fgmiss_0_19", None),
                               fgmiss_20_29=scoring_settings_dict.get("fgmiss_20_29", None),
                               fgmiss_30_39=scoring_settings_dict.get("fgmiss_30_39", None),
                               fgmiss_40_49=scoring_settings_dict.get("fgmiss_40_49", None),
                               fgmiss_50p=scoring_settings_dict.get("fgmiss_50p", None),
                               fg_ret_yd=scoring_settings_dict.get("fg_ret_yd", None),
                               pass_2pt=scoring_settings_dict["pass_2pt"],
                               pass_int=scoring_settings_dict["pass_int"],
                               pass_sack=scoring_settings_dict.get("pass_sack", None),
                               pass_cmp=scoring_settings_dict.get("pass_cmp", None),
                               pass_cmp_40p=scoring_settings_dict.get("pass_cmp_40p", None),
                               pass_inc=scoring_settings_dict.get("pass_inc", None),
                               pass_att=scoring_settings_dict.get("pass_att", None),
                               pass_yd=scoring_settings_dict["pass_yd"],
                               pass_td=scoring_settings_dict["pass_td"],
                               def_pass_def=scoring_settings_dict.get("def_pass_def", None),
                               def_td=scoring_settings_dict["def_td"],
                               def_st_fum_rec=scoring_settings_dict.get("def_st_fum_rec", None),
                               def_st_td=scoring_settings_dict.get("def_st_td", None),
                               def_st_ff=scoring_settings_dict.get("def_st_ff", None),
                               def_2pt=scoring_settings_dict.get("def_2pt", None),
                               st_fum_rec=scoring_settings_dict["st_fum_rec"],
                               st_ff=scoring_settings_dict["st_ff"],
                               st_tkl_solo=scoring_settings_dict.get("st_tkl_solo", None),
                               st_td=scoring_settings_dict["st_td"],
                               fum_rec=scoring_settings_dict["fum_rec"],
                               fum_lost=scoring_settings_dict["fum_lost"],
                               fum=scoring_settings_dict["fum"],
                               fum_ret_yd=scoring_settings_dict.get("fum_ret_yd", None),
                               idp_safe=scoring_settings_dict.get("idp_safe", None),
                               idp_ff=scoring_settings_dict.get("idp_ff", None),
                               idp_blk_kick=scoring_settings_dict.get("idp_blk_kick", None),
                               idp_int=scoring_settings_dict.get("idp_int", None),
                               idp_tkl=scoring_settings_dict.get("idp_tkl", None),
                               idp_def_td=scoring_settings_dict.get("idp_def_td", None),
                               idp_pass_def=scoring_settings_dict.get("idp_pass_def", None),
                               idp_fum_rec=scoring_settings_dict.get("idp_fum_rec", None),
                               idp_sack=scoring_settings_dict.get("idp_sack", None),
                               idp_tkl_ast=scoring_settings_dict.get("idp_tkl_ast", None),
                               idp_tkl_solo=scoring_settings_dict.get("idp_tkl_solo", None),
                               rush_att=scoring_settings_dict.get("rush_att", None),
                               pts_allow_0=scoring_settings_dict["pts_allow_0"],
                               pts_allow_1_6=scoring_settings_dict["pts_allow_1_6"],
                               pts_allow_7_13=scoring_settings_dict["pts_allow_7_13"],
                               pts_allow_14_20=scoring_settings_dict["pts_allow_14_20"],
                               pts_allow_21_27=scoring_settings_dict["pts_allow_21_27"],
                               pts_allow_28_34=scoring_settings_dict["pts_allow_28_34"],
                               pts_allow_35p=scoring_settings_dict["pts_allow_35p"],
                               rush_40p=scoring_settings_dict.get("rush_40p", None),
                               rush_2pt=scoring_settings_dict["rush_2pt"],
                               rush_yd=scoring_settings_dict["rush_yd"],
                               rush_td=scoring_settings_dict["rush_td"],
                               bonus_rush_yd_100=scoring_settings_dict.get("bonus_rush_yd_100", None),
                               bonus_rush_yd_200=scoring_settings_dict.get("bonus_rush_yd_200", None),
                               bonus_rec_yd_100=scoring_settings_dict.get("bonus_rec_yd_100", None),
                               bonus_rec_yd_200=scoring_settings_dict.get("bonus_rec_yd_200", None),
                               bonus_pass_yd_300=scoring_settings_dict.get("bonus_pass_yd_300", None),
                               bonus_pass_yd_400=scoring_settings_dict.get("bonus_pass_yd_400", None),
                               rec_yd=scoring_settings_dict["rec_yd"],
                               rec_2pt=scoring_settings_dict["rec_2pt"],
                               rec=scoring_settings_dict["rec"],
                               rec_td=scoring_settings_dict["rec_td"],
                               rec_40p=scoring_settings_dict.get("rec_40p", None),
                               tkl=scoring_settings_dict.get("tkl", None),
                               tkl_loss=scoring_settings_dict.get("tkl_loss", None),
                               tkl_solo=scoring_settings_dict.get("tkl_solo", None),
                               tkl_ast=scoring_settings_dict.get("tkl_ast", None),
                               int_ret_yd=scoring_settings_dict.get("int_ret_yd", None),
                               int=scoring_settings_dict["int"],
                               pr_td=scoring_settings_dict.get("pr_td", None),
                               pr_yd=scoring_settings_dict.get("pr_yd", None),
                               sack_yd=scoring_settings_dict.get("sack_yd", None),
                               sack=scoring_settings_dict["sack"],
                               kr_yd=scoring_settings_dict.get("kr_yd", None),
                               kr_td=scoring_settings_dict.get("kr_td", None),
                               blk_kick=scoring_settings_dict["blk_kick"],
                               blk_kick_ret_yd=scoring_settings_dict.get("blk_kick_ret_yd", None),
                               xpmiss=scoring_settings_dict.get("xpmiss", None),
                               ff=scoring_settings_dict["ff"],
                               qb_hit=scoring_settings_dict.get("qb_hit", None),
                               xpm=scoring_settings_dict["xpm"],
                               safe=scoring_settings_dict["safe"])
