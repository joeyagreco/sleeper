import unittest
from unittest import mock

from sleeper import LeagueAPIClient
from sleeper.enum.SeasonStatus import SeasonStatus
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.enum.nfl.NFLRosterPosition import NFLRosterPosition
from sleeper.exception.SleeperAPIException import SleeperAPIException
from sleeper.model.League import League
from sleeper.model.LeagueSettings import LeagueSettings
from sleeper.model.ScoringSettings import ScoringSettings
from test.helper.helper_classes import MockResponse


class TestLeagueAPIClient(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_league_happy_path(self, mock_requests_get):
        mock_dict = {
            "total_rosters": 12,
            "status": "in_season",
            "sport": "nfl",
            "shard": 679,
            "settings": {
                "max_keepers": 1,
                "draft_rounds": 3,
                "trade_review_days": 2,
                "reserve_allow_dnr": 0,
                "capacity_override": 0,
                "pick_trading": 1,
                "disable_trades": 1,
                "taxi_years": 0,
                "taxi_allow_vets": 0,
                "best_ball": 1,
                "disable_adds": 1,
                "waiver_type": 0,
                "bench_lock": 0,
                "reserve_allow_sus": 0,
                "type": 0,
                "reserve_allow_cov": 0,
                "waiver_clear_days": 2,
                "daily_waivers_last_ran": 17,
                "waiver_day_of_week": 2,
                "start_week": 1,
                "commissioner_direct_invite": 0,
                "playoff_teams": 6,
                "num_teams": 12,
                "reserve_slots": 0,
                "playoff_round_type": 0,
                "daily_waivers_hour": 0,
                "waiver_budget": 100,
                "reserve_allow_out": 0,
                "waiver_bid_min": 0,
                "offseason_adds": 0,
                "playoff_seed_type": 0,
                "daily_waivers": 0,
                "playoff_week_start": 15,
                "daily_waivers_days": 5461,
                "league_average_match": 0,
                "leg": 1,
                "trade_deadline": 11,
                "reserve_allow_doubtful": 0,
                "taxi_deadline": 0,
                "reserve_allow_na": 0,
                "taxi_slots": 0,
                "playoff_type": 0,
                "last_report": 1,
                "last_scored_leg": 3
            },
            "season_type": "regular",
            "season": "2022",
            "scoring_settings": {
                "pass_2pt": 2.0,
                "pass_int": -1.0,
                "fgmiss": -1.0,
                "fgmiss_0_19": -1.0,
                "fgmiss_20_29": -1.0,
                "fgmiss_30_39": -1.0,
                "fgmiss_40_49": -1.0,
                "fgmiss_50p": -1.0,
                "rec_yd": 0.1,
                "xpmiss": -1.0,
                "fgm_0_19": 3.0,
                "fgm_20_29": 3.0,
                "fgm_30_39": 3.0,
                "fgm_40_49": 4.0,
                "fgm_50p": 5.0,
                "blk_kick": 2.0,
                "blk_kick_ret_yd": 1.0,
                "pts_allow_7_13": 4.0,
                "ff": 1.0,
                "pts_allow_1_6": 7.0,
                "st_fum_rec": 1.0,
                "def_st_ff": 1.0,
                "st_ff": 1.0,
                "pts_allow_28_34": -1.0,
                "fum_rec": 2.0,
                "def_td": 6.0,
                "int": 2.0,
                "pts_allow_0": 10.0,
                "pts_allow_21_27": 0.0,
                "rec_2pt": 2.0,
                "rec": 1.0,
                "xpm": 1.0,
                "st_td": 6.0,
                "def_st_fum_rec": 1.0,
                "def_st_td": 6.0,
                "sack": 1.0,
                "fum_rec_td": 6.0,
                "rush_2pt": 2.0,
                "rec_td": 6.0,
                "pts_allow_35p": -4.0,
                "pts_allow_14_20": 1.0,
                "rush_yd": 0.1,
                "pass_yd": 0.04,
                "pass_td": 4.0,
                "rush_td": 6.0,
                "fum_lost": -2.0,
                "fum": 0.0,
                "safe": 2.0,
                "bonus_pass_yd_300": 1.0,
                "bonus_pass_yd_400": 1.0,
                "bonus_rec_yd_100": 1.0,
                "bonus_rec_yd_200": 1.0,
                "bonus_rush_yd_100": 1.0,
                "bonus_rush_yd_200": 1.0,
                "def_2pt": 1.0,
                "def_pass_def": 1.0,
                "fg_ret_yd": 1.0,
                "fgm": 1.0,
                "fum_ret_yd": 1.0,
                "idp_blk_kick": 1.0,
                "idp_def_td": 1.0,
                "idp_ff": 1.0,
                "idp_fum_rec": 1.0,
                "idp_int": 1.0,
                "idp_pass_def": 1.0,
                "idp_sack": 1.0,
                "idp_safe": 1.0,
                "idp_tkl": 1.0,
                "idp_tkl_ast": 1.0,
                "idp_tkl_solo": 1.0,
                "int_ret_yd": 1.0,
                "kr_td": 1.0,
                "kr_yd": 1.0,
                "pass_att": 1.0,
                "pass_cmp": 1.0,
                "pass_cmp_40p": 1.0,
                "pass_inc": 1.0,
                "pass_sack": 1.0,
                "pr_td": 1.0,
                "pr_yd": 1.0,
                "qb_hit": 1.0,
                "rec_40p": 1.0,
                "rush_40p": 1.0,
                "rush_att": 1.0,
                "sack_yd": 1.0,
                "st_tkl_solo": 1.0,
                "tkl": 1.0,
                "tkl_ast": 1.0,
                "tkl_loss": 1.0,
                "tkl_solo": 1.0,
                "yds_allow_0_100": 1.0,
                "yds_allow_100_199": 1.0,
                "yds_allow_200_299": 1.0,
                "yds_allow_300_349": 1.0,
                "yds_allow_350_399": 1.0,
                "yds_allow_400_449": 1.0,
                "yds_allow_450_499": 1.0,
                "yds_allow_500_549": 1.0,
                "yds_allow_550p": 1.0
            },
            "roster_positions": [
                "QB",
                "RB",
                "RB",
                "WR",
                "TE",
                "FLEX",
                "BN"
            ],
            "previous_league_id": "12345",
            "name": "R2 PooPoo DooDoo",
            "metadata": {
                "keeper_deadline": "0",
                "auto_continue": "off"
            },
            "loser_bracket_id": None,
            "league_id": "854528180957097984",
            "last_read_id": None,
            "last_pinned_message_id": "854538979343712256",
            "last_message_time": 1658185095507,
            "last_message_text_map": None,
            "last_message_id": "854893888614273024",
            "last_message_attachment": None,
            "last_author_is_bot": False,
            "last_author_id": "444590402142466048",
            "last_author_display_name": "BIGCELL561",
            "last_author_avatar": "9b69495def7b9b9d77e0a0126c22efbe",
            "group_id": None,
            "draft_id": "854528182030835712",
            "company_id": None,
            "bracket_id": None,
            "avatar": "d4ed6e3ae14b56422de8029566d51234"
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = LeagueAPIClient.get_league(league_id="12345")

        self.assertIsInstance(response, League)
        self.assertEqual("d4ed6e3ae14b56422de8029566d51234", response.avatar)
        self.assertEqual("854528182030835712", response.draft_id)
        self.assertEqual("854528180957097984", response.league_id)
        self.assertEqual("R2 PooPoo DooDoo", response.name)
        self.assertEqual("12345", response.previous_league_id)
        self.assertIsInstance(response.roster_positions, list)
        self.assertEqual(7, len(response.roster_positions))
        for nfl_roster_position in response.roster_positions:
            self.assertIsInstance(nfl_roster_position, NFLRosterPosition)
        self.assertIsInstance(response.scoring_settings, ScoringSettings)
        self.assertEqual(2.0, response.scoring_settings.blk_kick)
        self.assertEqual(1.0, response.scoring_settings.blk_kick_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.bonus_pass_yd_300)
        self.assertEqual(1.0, response.scoring_settings.bonus_pass_yd_400)
        self.assertEqual(1.0, response.scoring_settings.bonus_rec_yd_100)
        self.assertEqual(1.0, response.scoring_settings.bonus_rec_yd_200)
        self.assertEqual(1.0, response.scoring_settings.bonus_rush_yd_100)
        self.assertEqual(1.0, response.scoring_settings.bonus_rush_yd_200)
        self.assertEqual(1.0, response.scoring_settings.def_2pt)
        self.assertEqual(1.0, response.scoring_settings.def_pass_def)
        self.assertEqual(1.0, response.scoring_settings.def_st_ff)
        self.assertEqual(1.0, response.scoring_settings.def_st_fum_rec)
        self.assertEqual(6.0, response.scoring_settings.def_st_td)
        self.assertEqual(6.0, response.scoring_settings.def_td)
        self.assertEqual(1.0, response.scoring_settings.ff)
        self.assertEqual(1.0, response.scoring_settings.fg_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.fgm)
        self.assertEqual(3.0, response.scoring_settings.fgm_0_19)
        self.assertEqual(3.0, response.scoring_settings.fgm_20_29)
        self.assertEqual(3.0, response.scoring_settings.fgm_30_39)
        self.assertEqual(4.0, response.scoring_settings.fgm_40_49)
        self.assertEqual(5.0, response.scoring_settings.fgm_50p)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_0_19)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_20_29)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_30_39)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_40_49)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_50p)
        self.assertEqual(0.0, response.scoring_settings.fum)
        self.assertEqual(-2.0, response.scoring_settings.fum_lost)
        self.assertEqual(2.0, response.scoring_settings.fum_rec)
        self.assertEqual(1.0, response.scoring_settings.fum_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.idp_blk_kick)
        self.assertEqual(1.0, response.scoring_settings.idp_def_td)
        self.assertEqual(1.0, response.scoring_settings.idp_ff)
        self.assertEqual(1.0, response.scoring_settings.idp_fum_rec)
        self.assertEqual(1.0, response.scoring_settings.idp_int)
        self.assertEqual(1.0, response.scoring_settings.idp_pass_def)
        self.assertEqual(1.0, response.scoring_settings.idp_sack)
        self.assertEqual(1.0, response.scoring_settings.idp_safe)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl_ast)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl_solo)
        self.assertEqual(2.0, response.scoring_settings.int)
        self.assertEqual(1.0, response.scoring_settings.int_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.kr_td)
        self.assertEqual(1.0, response.scoring_settings.kr_yd)
        self.assertEqual(2.0, response.scoring_settings.pass_2pt)
        self.assertEqual(1.0, response.scoring_settings.pass_att)
        self.assertEqual(1.0, response.scoring_settings.pass_cmp)
        self.assertEqual(1.0, response.scoring_settings.pass_cmp_40p)
        self.assertEqual(1.0, response.scoring_settings.pass_inc)
        self.assertEqual(-1.0, response.scoring_settings.pass_int)
        self.assertEqual(1.0, response.scoring_settings.pass_sack)
        self.assertEqual(4.0, response.scoring_settings.pass_td)
        self.assertEqual(0.04, response.scoring_settings.pass_yd)
        self.assertEqual(1.0, response.scoring_settings.pr_td)
        self.assertEqual(1.0, response.scoring_settings.pr_yd)
        self.assertEqual(10.0, response.scoring_settings.pts_allow_0)
        self.assertEqual(1.0, response.scoring_settings.pts_allow_14_20)
        self.assertEqual(7.0, response.scoring_settings.pts_allow_1_6)
        self.assertEqual(0.0, response.scoring_settings.pts_allow_21_27)
        self.assertEqual(-1.0, response.scoring_settings.pts_allow_28_34)
        self.assertEqual(-4.0, response.scoring_settings.pts_allow_35p)
        self.assertEqual(4.0, response.scoring_settings.pts_allow_7_13)
        self.assertEqual(1.0, response.scoring_settings.qb_hit)
        self.assertEqual(1.0, response.scoring_settings.rec)
        self.assertEqual(2.0, response.scoring_settings.rec_2pt)
        self.assertEqual(1.0, response.scoring_settings.rec_40p)
        self.assertEqual(6.0, response.scoring_settings.rec_td)
        self.assertEqual(0.1, response.scoring_settings.rec_yd)
        self.assertEqual(2.0, response.scoring_settings.rush_2pt)
        self.assertEqual(1.0, response.scoring_settings.rush_40p)
        self.assertEqual(1.0, response.scoring_settings.rush_att)
        self.assertEqual(6.0, response.scoring_settings.rush_td)
        self.assertEqual(0.1, response.scoring_settings.rush_yd)
        self.assertEqual(1.0, response.scoring_settings.sack)
        self.assertEqual(1.0, response.scoring_settings.sack_yd)
        self.assertEqual(2.0, response.scoring_settings.safe)
        self.assertEqual(1.0, response.scoring_settings.st_ff)
        self.assertEqual(1.0, response.scoring_settings.st_fum_rec)
        self.assertEqual(6.0, response.scoring_settings.st_td)
        self.assertEqual(1.0, response.scoring_settings.st_tkl_solo)
        self.assertEqual(1.0, response.scoring_settings.tkl)
        self.assertEqual(1.0, response.scoring_settings.tkl_ast)
        self.assertEqual(1.0, response.scoring_settings.tkl_loss)
        self.assertEqual(1.0, response.scoring_settings.tkl_solo)
        self.assertEqual(1.0, response.scoring_settings.xpm)
        self.assertEqual(-1.0, response.scoring_settings.xpmiss)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_0_100)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_100_199)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_200_299)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_300_349)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_350_399)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_400_449)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_450_499)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_500_549)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_550p)
        self.assertEqual("2022", response.season)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertIsInstance(response.settings, LeagueSettings)
        self.assertEqual(3, response.settings.draft_rounds)
        self.assertEqual(1, response.settings.last_report)
        self.assertEqual(3, response.settings.last_scored_leg)
        self.assertEqual(1, response.settings.leg)
        self.assertEqual(1, response.settings.max_keepers)
        self.assertEqual(12, response.settings.num_teams)
        self.assertEqual(0, response.settings.offseason_adds)
        self.assertEqual(1, response.settings.pick_trading)
        self.assertEqual(6, response.settings.playoff_teams)
        self.assertEqual(15, response.settings.playoff_week_start)
        self.assertEqual(0, response.settings.reserve_allow_out)
        self.assertEqual(0, response.settings.reserve_slots)
        self.assertEqual(1, response.settings.start_week)
        self.assertEqual(11, response.settings.trade_deadline)
        self.assertEqual(2, response.settings.trade_review_days)
        self.assertEqual(0, response.settings.type)
        self.assertEqual(100, response.settings.waiver_budget)
        self.assertEqual(2, response.settings.waiver_clear_days)
        self.assertEqual(2, response.settings.waiver_day_of_week)
        self.assertEqual(0, response.settings.waiver_type)
        self.assertEqual(0, response.settings.bench_lock)
        self.assertEqual(1, response.settings.best_ball)
        self.assertEqual(0, response.settings.capacity_override)
        self.assertEqual(0, response.settings.commissioner_direct_invite)
        self.assertEqual(0, response.settings.daily_waivers)
        self.assertEqual(5461, response.settings.daily_waivers_days)
        self.assertEqual(0, response.settings.daily_waivers_hour)
        self.assertEqual(17, response.settings.daily_waivers_last_ran)
        self.assertEqual(1, response.settings.disable_adds)
        self.assertEqual(1, response.settings.disable_trades)
        self.assertEqual(0, response.settings.league_average_match)
        self.assertEqual(0, response.settings.playoff_round_type)
        self.assertEqual(0, response.settings.playoff_seed_type)
        self.assertEqual(0, response.settings.playoff_type)
        self.assertEqual(0, response.settings.reserve_allow_cov)
        self.assertEqual(0, response.settings.reserve_allow_dnr)
        self.assertEqual(0, response.settings.reserve_allow_na)
        self.assertEqual(0, response.settings.reserve_allow_sus)
        self.assertEqual(0, response.settings.taxi_allow_vets)
        self.assertEqual(0, response.settings.taxi_slots)
        self.assertEqual(0, response.settings.taxi_years)
        self.assertEqual(0, response.settings.waiver_bid_min)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonStatus.IN_SEASON, response.status)
        self.assertEqual(12, response.total_rosters)

    @mock.patch("requests.get")
    def test_get_league_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            LeagueAPIClient.get_league(league_id="12345")
        self.assertEqual("Could not get League with league_id '12345'.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_league_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(SleeperAPIException) as context:
            LeagueAPIClient.get_league(league_id="12345")
        self.assertEqual("Got bad status code (404) from request.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_user_leagues_for_year_happy_path(self, mock_requests_get):
        mock_dict = [
            {
                "total_rosters": 12,
                "status": "in_season",
                "sport": "nfl",
                "shard": 679,
                "settings": {
                    "max_keepers": 1,
                    "draft_rounds": 3,
                    "trade_review_days": 2,
                    "reserve_allow_dnr": 0,
                    "capacity_override": 0,
                    "pick_trading": 1,
                    "disable_trades": 1,
                    "taxi_years": 0,
                    "taxi_allow_vets": 0,
                    "best_ball": 1,
                    "disable_adds": 1,
                    "waiver_type": 0,
                    "bench_lock": 0,
                    "reserve_allow_sus": 0,
                    "type": 0,
                    "reserve_allow_cov": 0,
                    "waiver_clear_days": 2,
                    "daily_waivers_last_ran": 17,
                    "waiver_day_of_week": 2,
                    "start_week": 1,
                    "commissioner_direct_invite": 0,
                    "playoff_teams": 6,
                    "num_teams": 12,
                    "reserve_slots": 0,
                    "playoff_round_type": 0,
                    "daily_waivers_hour": 0,
                    "waiver_budget": 100,
                    "reserve_allow_out": 0,
                    "waiver_bid_min": 0,
                    "offseason_adds": 0,
                    "playoff_seed_type": 0,
                    "daily_waivers": 0,
                    "playoff_week_start": 15,
                    "daily_waivers_days": 5461,
                    "league_average_match": 0,
                    "leg": 1,
                    "trade_deadline": 11,
                    "reserve_allow_doubtful": 0,
                    "taxi_deadline": 0,
                    "reserve_allow_na": 0,
                    "taxi_slots": 0,
                    "playoff_type": 0,
                    "last_report": 1,
                    "last_scored_leg": 3
                },
                "season_type": "regular",
                "season": "2022",
                "scoring_settings": {
                    "pass_2pt": 2.0,
                    "pass_int": -1.0,
                    "fgmiss": -1.0,
                    "fgmiss_0_19": -1.0,
                    "fgmiss_20_29": -1.0,
                    "fgmiss_30_39": -1.0,
                    "fgmiss_40_49": -1.0,
                    "fgmiss_50p": -1.0,
                    "rec_yd": 0.1,
                    "xpmiss": -1.0,
                    "fgm_0_19": 3.0,
                    "fgm_20_29": 3.0,
                    "fgm_30_39": 3.0,
                    "fgm_40_49": 4.0,
                    "fgm_50p": 5.0,
                    "blk_kick": 2.0,
                    "blk_kick_ret_yd": 1.0,
                    "pts_allow_7_13": 4.0,
                    "ff": 1.0,
                    "pts_allow_1_6": 7.0,
                    "st_fum_rec": 1.0,
                    "def_st_ff": 1.0,
                    "st_ff": 1.0,
                    "pts_allow_28_34": -1.0,
                    "fum_rec": 2.0,
                    "def_td": 6.0,
                    "int": 2.0,
                    "pts_allow_0": 10.0,
                    "pts_allow_21_27": 0.0,
                    "rec_2pt": 2.0,
                    "rec": 1.0,
                    "xpm": 1.0,
                    "st_td": 6.0,
                    "def_st_fum_rec": 1.0,
                    "def_st_td": 6.0,
                    "sack": 1.0,
                    "fum_rec_td": 6.0,
                    "rush_2pt": 2.0,
                    "rec_td": 6.0,
                    "pts_allow_35p": -4.0,
                    "pts_allow_14_20": 1.0,
                    "rush_yd": 0.1,
                    "pass_yd": 0.04,
                    "pass_td": 4.0,
                    "rush_td": 6.0,
                    "fum_lost": -2.0,
                    "fum": 0.0,
                    "safe": 2.0,
                    "bonus_pass_yd_300": 1.0,
                    "bonus_pass_yd_400": 1.0,
                    "bonus_rec_yd_100": 1.0,
                    "bonus_rec_yd_200": 1.0,
                    "bonus_rush_yd_100": 1.0,
                    "bonus_rush_yd_200": 1.0,
                    "def_2pt": 1.0,
                    "def_pass_def": 1.0,
                    "fg_ret_yd": 1.0,
                    "fgm": 1.0,
                    "fum_ret_yd": 1.0,
                    "idp_blk_kick": 1.0,
                    "idp_def_td": 1.0,
                    "idp_ff": 1.0,
                    "idp_fum_rec": 1.0,
                    "idp_int": 1.0,
                    "idp_pass_def": 1.0,
                    "idp_sack": 1.0,
                    "idp_safe": 1.0,
                    "idp_tkl": 1.0,
                    "idp_tkl_ast": 1.0,
                    "idp_tkl_solo": 1.0,
                    "int_ret_yd": 1.0,
                    "kr_td": 1.0,
                    "kr_yd": 1.0,
                    "pass_att": 1.0,
                    "pass_cmp": 1.0,
                    "pass_cmp_40p": 1.0,
                    "pass_inc": 1.0,
                    "pass_sack": 1.0,
                    "pr_td": 1.0,
                    "pr_yd": 1.0,
                    "qb_hit": 1.0,
                    "rec_40p": 1.0,
                    "rush_40p": 1.0,
                    "rush_att": 1.0,
                    "sack_yd": 1.0,
                    "st_tkl_solo": 1.0,
                    "tkl": 1.0,
                    "tkl_ast": 1.0,
                    "tkl_loss": 1.0,
                    "tkl_solo": 1.0,
                    "yds_allow_0_100": 1.0,
                    "yds_allow_100_199": 1.0,
                    "yds_allow_200_299": 1.0,
                    "yds_allow_300_349": 1.0,
                    "yds_allow_350_399": 1.0,
                    "yds_allow_400_449": 1.0,
                    "yds_allow_450_499": 1.0,
                    "yds_allow_500_549": 1.0,
                    "yds_allow_550p": 1.0
                },
                "roster_positions": [
                    "QB",
                    "RB",
                    "RB",
                    "WR",
                    "TE",
                    "FLEX",
                    "BN"
                ],
                "previous_league_id": "12345",
                "name": "R2 PooPoo DooDoo",
                "metadata": {
                    "keeper_deadline": "0",
                    "auto_continue": "off"
                },
                "loser_bracket_id": None,
                "league_id": "854528180957097984",
                "last_read_id": None,
                "last_pinned_message_id": "854538979343712256",
                "last_message_time": 1658185095507,
                "last_message_text_map": None,
                "last_message_id": "854893888614273024",
                "last_message_attachment": None,
                "last_author_is_bot": False,
                "last_author_id": "444590402142466048",
                "last_author_display_name": "BIGCELL561",
                "last_author_avatar": "9b69495def7b9b9d77e0a0126c22efbe",
                "group_id": None,
                "draft_id": "854528182030835712",
                "company_id": None,
                "bracket_id": None,
                "avatar": "d4ed6e3ae14b56422de8029566d51234"
            }
        ]
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = LeagueAPIClient.get_user_leagues_for_year(user_id="12345", sport=Sport.NFL, year="2020")[0]

        self.assertIsInstance(response, League)
        self.assertEqual("d4ed6e3ae14b56422de8029566d51234", response.avatar)
        self.assertEqual("854528182030835712", response.draft_id)
        self.assertEqual("854528180957097984", response.league_id)
        self.assertEqual("R2 PooPoo DooDoo", response.name)
        self.assertEqual("12345", response.previous_league_id)
        self.assertIsInstance(response.roster_positions, list)
        self.assertEqual(7, len(response.roster_positions))
        for nfl_roster_position in response.roster_positions:
            self.assertIsInstance(nfl_roster_position, NFLRosterPosition)
        self.assertIsInstance(response.scoring_settings, ScoringSettings)
        self.assertEqual(2.0, response.scoring_settings.blk_kick)
        self.assertEqual(1.0, response.scoring_settings.blk_kick_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.bonus_pass_yd_300)
        self.assertEqual(1.0, response.scoring_settings.bonus_pass_yd_400)
        self.assertEqual(1.0, response.scoring_settings.bonus_rec_yd_100)
        self.assertEqual(1.0, response.scoring_settings.bonus_rec_yd_200)
        self.assertEqual(1.0, response.scoring_settings.bonus_rush_yd_100)
        self.assertEqual(1.0, response.scoring_settings.bonus_rush_yd_200)
        self.assertEqual(1.0, response.scoring_settings.def_2pt)
        self.assertEqual(1.0, response.scoring_settings.def_pass_def)
        self.assertEqual(1.0, response.scoring_settings.def_st_ff)
        self.assertEqual(1.0, response.scoring_settings.def_st_fum_rec)
        self.assertEqual(6.0, response.scoring_settings.def_st_td)
        self.assertEqual(6.0, response.scoring_settings.def_td)
        self.assertEqual(1.0, response.scoring_settings.ff)
        self.assertEqual(1.0, response.scoring_settings.fg_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.fgm)
        self.assertEqual(3.0, response.scoring_settings.fgm_0_19)
        self.assertEqual(3.0, response.scoring_settings.fgm_20_29)
        self.assertEqual(3.0, response.scoring_settings.fgm_30_39)
        self.assertEqual(4.0, response.scoring_settings.fgm_40_49)
        self.assertEqual(5.0, response.scoring_settings.fgm_50p)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_0_19)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_20_29)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_30_39)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_40_49)
        self.assertEqual(-1.0, response.scoring_settings.fgmiss_50p)
        self.assertEqual(0.0, response.scoring_settings.fum)
        self.assertEqual(-2.0, response.scoring_settings.fum_lost)
        self.assertEqual(2.0, response.scoring_settings.fum_rec)
        self.assertEqual(1.0, response.scoring_settings.fum_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.idp_blk_kick)
        self.assertEqual(1.0, response.scoring_settings.idp_def_td)
        self.assertEqual(1.0, response.scoring_settings.idp_ff)
        self.assertEqual(1.0, response.scoring_settings.idp_fum_rec)
        self.assertEqual(1.0, response.scoring_settings.idp_int)
        self.assertEqual(1.0, response.scoring_settings.idp_pass_def)
        self.assertEqual(1.0, response.scoring_settings.idp_sack)
        self.assertEqual(1.0, response.scoring_settings.idp_safe)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl_ast)
        self.assertEqual(1.0, response.scoring_settings.idp_tkl_solo)
        self.assertEqual(2.0, response.scoring_settings.int)
        self.assertEqual(1.0, response.scoring_settings.int_ret_yd)
        self.assertEqual(1.0, response.scoring_settings.kr_td)
        self.assertEqual(1.0, response.scoring_settings.kr_yd)
        self.assertEqual(2.0, response.scoring_settings.pass_2pt)
        self.assertEqual(1.0, response.scoring_settings.pass_att)
        self.assertEqual(1.0, response.scoring_settings.pass_cmp)
        self.assertEqual(1.0, response.scoring_settings.pass_cmp_40p)
        self.assertEqual(1.0, response.scoring_settings.pass_inc)
        self.assertEqual(-1.0, response.scoring_settings.pass_int)
        self.assertEqual(1.0, response.scoring_settings.pass_sack)
        self.assertEqual(4.0, response.scoring_settings.pass_td)
        self.assertEqual(0.04, response.scoring_settings.pass_yd)
        self.assertEqual(1.0, response.scoring_settings.pr_td)
        self.assertEqual(1.0, response.scoring_settings.pr_yd)
        self.assertEqual(10.0, response.scoring_settings.pts_allow_0)
        self.assertEqual(1.0, response.scoring_settings.pts_allow_14_20)
        self.assertEqual(7.0, response.scoring_settings.pts_allow_1_6)
        self.assertEqual(0.0, response.scoring_settings.pts_allow_21_27)
        self.assertEqual(-1.0, response.scoring_settings.pts_allow_28_34)
        self.assertEqual(-4.0, response.scoring_settings.pts_allow_35p)
        self.assertEqual(4.0, response.scoring_settings.pts_allow_7_13)
        self.assertEqual(1.0, response.scoring_settings.qb_hit)
        self.assertEqual(1.0, response.scoring_settings.rec)
        self.assertEqual(2.0, response.scoring_settings.rec_2pt)
        self.assertEqual(1.0, response.scoring_settings.rec_40p)
        self.assertEqual(6.0, response.scoring_settings.rec_td)
        self.assertEqual(0.1, response.scoring_settings.rec_yd)
        self.assertEqual(2.0, response.scoring_settings.rush_2pt)
        self.assertEqual(1.0, response.scoring_settings.rush_40p)
        self.assertEqual(1.0, response.scoring_settings.rush_att)
        self.assertEqual(6.0, response.scoring_settings.rush_td)
        self.assertEqual(0.1, response.scoring_settings.rush_yd)
        self.assertEqual(1.0, response.scoring_settings.sack)
        self.assertEqual(1.0, response.scoring_settings.sack_yd)
        self.assertEqual(2.0, response.scoring_settings.safe)
        self.assertEqual(1.0, response.scoring_settings.st_ff)
        self.assertEqual(1.0, response.scoring_settings.st_fum_rec)
        self.assertEqual(6.0, response.scoring_settings.st_td)
        self.assertEqual(1.0, response.scoring_settings.st_tkl_solo)
        self.assertEqual(1.0, response.scoring_settings.tkl)
        self.assertEqual(1.0, response.scoring_settings.tkl_ast)
        self.assertEqual(1.0, response.scoring_settings.tkl_loss)
        self.assertEqual(1.0, response.scoring_settings.tkl_solo)
        self.assertEqual(1.0, response.scoring_settings.xpm)
        self.assertEqual(-1.0, response.scoring_settings.xpmiss)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_0_100)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_100_199)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_200_299)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_300_349)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_350_399)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_400_449)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_450_499)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_500_549)
        self.assertEqual(1.0, response.scoring_settings.yds_allow_550p)
        self.assertEqual("2022", response.season)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertIsInstance(response.settings, LeagueSettings)
        self.assertEqual(3, response.settings.draft_rounds)
        self.assertEqual(1, response.settings.last_report)
        self.assertEqual(3, response.settings.last_scored_leg)
        self.assertEqual(1, response.settings.leg)
        self.assertEqual(1, response.settings.max_keepers)
        self.assertEqual(12, response.settings.num_teams)
        self.assertEqual(0, response.settings.offseason_adds)
        self.assertEqual(1, response.settings.pick_trading)
        self.assertEqual(6, response.settings.playoff_teams)
        self.assertEqual(15, response.settings.playoff_week_start)
        self.assertEqual(0, response.settings.reserve_allow_out)
        self.assertEqual(0, response.settings.reserve_slots)
        self.assertEqual(1, response.settings.start_week)
        self.assertEqual(11, response.settings.trade_deadline)
        self.assertEqual(2, response.settings.trade_review_days)
        self.assertEqual(0, response.settings.type)
        self.assertEqual(100, response.settings.waiver_budget)
        self.assertEqual(2, response.settings.waiver_clear_days)
        self.assertEqual(2, response.settings.waiver_day_of_week)
        self.assertEqual(0, response.settings.waiver_type)
        self.assertEqual(0, response.settings.bench_lock)
        self.assertEqual(1, response.settings.best_ball)
        self.assertEqual(0, response.settings.capacity_override)
        self.assertEqual(0, response.settings.commissioner_direct_invite)
        self.assertEqual(0, response.settings.daily_waivers)
        self.assertEqual(5461, response.settings.daily_waivers_days)
        self.assertEqual(0, response.settings.daily_waivers_hour)
        self.assertEqual(17, response.settings.daily_waivers_last_ran)
        self.assertEqual(1, response.settings.disable_adds)
        self.assertEqual(1, response.settings.disable_trades)
        self.assertEqual(0, response.settings.league_average_match)
        self.assertEqual(0, response.settings.playoff_round_type)
        self.assertEqual(0, response.settings.playoff_seed_type)
        self.assertEqual(0, response.settings.playoff_type)
        self.assertEqual(0, response.settings.reserve_allow_cov)
        self.assertEqual(0, response.settings.reserve_allow_dnr)
        self.assertEqual(0, response.settings.reserve_allow_na)
        self.assertEqual(0, response.settings.reserve_allow_sus)
        self.assertEqual(0, response.settings.taxi_allow_vets)
        self.assertEqual(0, response.settings.taxi_slots)
        self.assertEqual(0, response.settings.taxi_years)
        self.assertEqual(0, response.settings.waiver_bid_min)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonStatus.IN_SEASON, response.status)
        self.assertEqual(12, response.total_rosters)

    @mock.patch("requests.get")
    def test_get_league_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            LeagueAPIClient.get_user_leagues_for_year(user_id="12345", sport=Sport.NFL, year="2020")
        self.assertEqual("Could not get user Leagues for user_id '12345', sport 'NFL', and year '2020'.",
                         str(context.exception))

    @mock.patch("requests.get")
    def test_get_league_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(SleeperAPIException) as context:
            LeagueAPIClient.get_user_leagues_for_year(user_id="12345", sport=Sport.NFL, year="2020")
        self.assertEqual("Got bad status code (404) from request.", str(context.exception))
