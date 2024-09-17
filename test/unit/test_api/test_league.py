import unittest
from unittest.mock import patch

from sleeper.api.league import (
    get_league,
    get_matchups_for_week,
    get_rosters,
    get_user_leagues_for_year,
    get_users_in_league,
)
from sleeper.enum import Sport
from test.unit.helper.helper_classes import MockResponse


class TestLeague(unittest.TestCase):
    @patch("requests.get")
    def test_get_league(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_league(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345"
        )

    @patch("requests.get")
    def test_get_user_leagues_for_year(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_user_leagues_for_year(
            user_id="12345", sport=Sport.NFL, year=2024
        )

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/user/12345/leagues/nfl/2024"
        )

    @patch("requests.get")
    def test_get_rosters(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_rosters(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/rosters"
        )

    @patch("requests.get")
    def test_get_users_in_league(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_users_in_league(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/users"
        )

    @patch("requests.get")
    def test_get_matchups_for_week(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_matchups_for_week(league_id="12345", week=1)

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/matchups/1"
        )
