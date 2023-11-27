import os
import tempfile
import unittest
from test.helper.helper_classes import MockResponse
from unittest import mock

from sleeper.api.unofficial import UPlayerAPIClient
from sleeper.enum import Category, Company, SeasonType
from sleeper.enum.nfl import NFLPosition, NFLTeam
from sleeper.enum.Sport import Sport
from sleeper.model import Player, PlayerStats
from sleeper.model.nfl import NFLStats


class TestUPlayerAPIClient(unittest.TestCase):
    PATH_TO_TEST_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "files", "api")
    )

    @mock.patch("requests.get")
    def test_get_player_stats_no_week_given_happy_path(self, mock_requests_get):
        mock_dict = {
            "team": "LAR",
            "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
            "sport": "nfl",
            "season_type": "regular",
            "season": "2021",
            "player_id": "1234",
            "player": {
                "years_exp": 1,
                "team": "LAR",
                "position": "WR",
                "news_updated": 1234,
                "last_name": "ln",
                "first_name": "fn",
                "fantasy_positions": ["WR"],
            },
            "game_id": "season",
            "company": "rotowire",
            "category": "stat",
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UPlayerAPIClient.get_player_stats(
            sport=Sport.NFL, player_id="1234", season="2021"
        )

        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("season", response.game_id)
        self.assertEqual(Company.ROTOWIRE, response.company)
        self.assertEqual(Category.STAT, response.category)

    @mock.patch("requests.get")
    def test_get_player_stats_week_is_given_happy_path(self, mock_requests_get):
        mock_dict = {
            "week": 1,
            "team": "LAR",
            "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
            "sport": "nfl",
            "season_type": "regular",
            "season": "2021",
            "opponent": "SEA",
            "player_id": "1234",
            "player": {
                "years_exp": 1,
                "team": "LAR",
                "position": "WR",
                "news_updated": 1234,
                "last_name": "ln",
                "first_name": "fn",
                "fantasy_positions": ["WR"],
            },
            "game_id": "1234",
            "company": "sportradar",
            "category": "stat",
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UPlayerAPIClient.get_player_stats(
            sport=Sport.NFL, player_id="1234", season="2021", week=1
        )

        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1, response.week)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("1234", response.game_id)
        self.assertEqual(Company.SPORTRADAR, response.company)
        self.assertEqual(Category.STAT, response.category)
        self.assertEqual(NFLTeam.SEA, response.opponent)

    @mock.patch("requests.get")
    def test_get_player_projections_no_week_given_happy_path(self, mock_requests_get):
        mock_dict = {
            "team": "LAR",
            "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
            "sport": "nfl",
            "season_type": "regular",
            "season": "2021",
            "player_id": "1234",
            "player": {
                "years_exp": 1,
                "team": "LAR",
                "position": "WR",
                "news_updated": 1234,
                "last_name": "ln",
                "first_name": "fn",
                "fantasy_positions": ["WR"],
            },
            "game_id": "season",
            "company": "rotowire",
            "category": "proj",
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UPlayerAPIClient.get_player_projections(
            sport=Sport.NFL, player_id="1234", season="2021"
        )

        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("season", response.game_id)
        self.assertEqual(Company.ROTOWIRE, response.company)
        self.assertEqual(Category.PROJ, response.category)

    @mock.patch("requests.get")
    def test_get_player_projections_week_is_given_happy_path(self, mock_requests_get):
        mock_dict = {
            "week": 1,
            "team": "LAR",
            "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
            "sport": "nfl",
            "season_type": "regular",
            "season": "2021",
            "opponent": "SEA",
            "player_id": "1234",
            "player": {
                "years_exp": 1,
                "team": "LAR",
                "position": "WR",
                "news_updated": 1234,
                "last_name": "ln",
                "first_name": "fn",
                "fantasy_positions": ["WR"],
            },
            "game_id": "1234",
            "company": "sportradar",
            "category": "proj",
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UPlayerAPIClient.get_player_stats(
            sport=Sport.NFL, player_id="1234", season="2021", week=1
        )

        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1, response.week)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("1234", response.game_id)
        self.assertEqual(Company.SPORTRADAR, response.company)
        self.assertEqual(Category.PROJ, response.category)
        self.assertEqual(NFLTeam.SEA, response.opponent)

    @mock.patch("requests.get")
    def test_get_all_player_stats_happy_path(self, mock_requests_get):
        mock_list = [
            {
                "week": 1,
                "team": "LAR",
                "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
                "sport": "nfl",
                "season_type": "regular",
                "season": "2021",
                "opponent": "SEA",
                "player_id": "1234",
                "player": {
                    "years_exp": 1,
                    "team": "LAR",
                    "position": "WR",
                    "news_updated": 1234,
                    "last_name": "ln",
                    "first_name": "fn",
                    "fantasy_positions": ["WR"],
                },
                "game_id": "1234",
                "company": "sportradar",
                "category": "stat",
            }
        ]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response_list = UPlayerAPIClient.get_all_player_stats(
            sport=Sport.NFL, season="2021", week=1
        )
        response = response_list[0]

        self.assertIsInstance(response_list, list)
        self.assertEqual(1, len(response_list))
        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1, response.week)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("1234", response.game_id)
        self.assertEqual(Company.SPORTRADAR, response.company)
        self.assertEqual(Category.STAT, response.category)
        self.assertEqual(NFLTeam.SEA, response.opponent)

    @mock.patch("requests.get")
    def test_get_all_player_projections_happy_path(self, mock_requests_get):
        mock_list = [
            {
                "week": 1,
                "team": "LAR",
                "stats": {"rush_yd": 1.0, "rush_fd": 2.0, "rush_att": 3.0},
                "sport": "nfl",
                "season_type": "regular",
                "season": "2021",
                "opponent": "SEA",
                "player_id": "1234",
                "player": {
                    "years_exp": 1,
                    "team": "LAR",
                    "position": "WR",
                    "news_updated": 1234,
                    "last_name": "ln",
                    "first_name": "fn",
                    "fantasy_positions": ["WR"],
                },
                "game_id": "1234",
                "company": "sportradar",
                "category": "proj",
            }
        ]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response_list = UPlayerAPIClient.get_all_player_projections(
            sport=Sport.NFL, season="2021", week=1
        )
        response = response_list[0]

        self.assertIsInstance(response_list, list)
        self.assertEqual(1, len(response_list))
        self.assertIsInstance(response, PlayerStats)
        self.assertEqual(NFLTeam.LAR, response.team)
        self.assertIsInstance(response.stats, NFLStats)
        self.assertEqual(1, response.week)
        self.assertEqual(1.0, response.stats.rush_yd)
        self.assertEqual(2.0, response.stats.rush_fd)
        self.assertEqual(3.0, response.stats.rush_att)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertEqual("2021", response.season)
        self.assertEqual("1234", response.player_id)
        self.assertIsInstance(response.player, Player)
        self.assertEqual(1, response.player.years_exp)
        self.assertEqual(NFLTeam.LAR, response.player.team)
        self.assertEqual(NFLPosition.WR, response.player.position)
        self.assertEqual(1234, response.player.news_updated)
        self.assertIsNone(response.player.metadata)
        self.assertEqual("ln", response.player.last_name)
        self.assertEqual("fn", response.player.first_name)
        self.assertEqual([NFLPosition.WR], response.player.fantasy_positions)
        self.assertEqual("1234", response.game_id)
        self.assertEqual(Company.SPORTRADAR, response.company)
        self.assertEqual(Category.PROJ, response.category)
        self.assertEqual(NFLTeam.SEA, response.opponent)

    @mock.patch("requests.get")
    def test_get_player_head_shot_happy_path(self, mock_requests_get):
        with open(os.path.join(self.PATH_TO_TEST_DIR, "test.png"), "rb") as image:
            f = image.read()
            original_image_bytes = bytearray(f)
        mock_response = MockResponse(dict(), 200, content=original_image_bytes)
        mock_requests_get.return_value = mock_response

        with tempfile.TemporaryDirectory() as temp_dir:
            full_image_path = os.path.join(temp_dir, "tmp.png")
            UPlayerAPIClient.get_player_head_shot(
                sport=Sport.NFL, player_id="1234", save_to_path=full_image_path
            )

            with open(full_image_path, "rb") as image:
                f = image.read()
                saved_image_bytes = bytearray(f)
            self.assertEqual(original_image_bytes, saved_image_bytes)
            self.assertTrue(os.path.exists(full_image_path))
