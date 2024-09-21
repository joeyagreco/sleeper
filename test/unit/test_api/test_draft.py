import unittest
from unittest.mock import patch

from sleeper.api import (
    get_draft,
    get_drafts_in_league,
    get_player_draft_picks,
    get_traded_draft_picks,
    get_user_drafts_for_year,
)
from test.unit.helper.helper_classes import MockResponse


class TestDraft(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_drafts_for_year_happy_path(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_user_drafts_for_year(user_id="user_id", sport="nfl", year=2020)

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/user/user_id/drafts/nfl/2020"
        )

    @patch("requests.get")
    def test_get_drafts_in_league(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_drafts_in_league(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/drafts"
        )

    @patch("requests.get")
    def test_get_draft(self, mock_requests_get):
        mock_dict = {"foo": "bar"}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_draft(draft_id="12345")

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/draft/12345"
        )

    @patch("requests.get")
    def test_get_player_draft_picks(self, mock_requests_get):
        mock_dict = {"foo": "bar"}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_player_draft_picks(draft_id="12345")

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/draft/12345/picks"
        )

    @patch("requests.get")
    def test_get_traded_draft_picks(self, mock_requests_get):
        mock_dict = {"foo": "bar"}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_traded_draft_picks(draft_id="12345")

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/draft/12345/traded_picks"
        )
