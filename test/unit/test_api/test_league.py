import unittest
from unittest.mock import patch

from sleeper.api import (
    get_league,
    get_losers_bracket,
    get_matchups_for_week,
    get_rosters,
    get_sport_state,
    get_traded_picks,
    get_transactions,
    get_user_leagues_for_year,
    get_users_in_league,
    get_winners_bracket,
)
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

        response = get_user_leagues_for_year(user_id="12345", sport="nfl", year=2024)

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

    @patch("requests.get")
    def test_get_winners_bracket(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_winners_bracket(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/winners_bracket"
        )

    @patch("requests.get")
    def test_get_losers_bracket(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_losers_bracket(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/losers_bracket"
        )

    @patch("requests.get")
    def test_get_transactions(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_transactions(league_id="12345", week=1)

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/transactions/1"
        )

    @patch("requests.get")
    def test_get_traded_picks(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_traded_picks(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/traded_picks"
        )

    @patch("requests.get")
    def test_get_sport_state(self, mock_requests_get):
        mock_dict = {"foo": "bar"}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_sport_state(sport="nfl")

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/state/nfl"
        )
