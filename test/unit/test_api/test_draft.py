import unittest

from sleeper.api.draft import get_draft, get_drafts_in_league, get_user_drafts_for_year
from sleeper.enum.Sport import Sport
from test.unit.helper.helper_classes import MockResponse


class TestDraft(unittest.TestCase):
    @unittest.mock.patch("requests.get")
    def test_get_user_drafts_for_year_happy_path(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_user_drafts_for_year(
            user_id="user_id", sport=Sport.NFL, year="2020"
        )

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/user/user_id/drafts/nfl/2020"
        )

    @unittest.mock.patch("requests.get")
    def test_get_drafts_in_league(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_drafts_in_league(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345/drafts"
        )

    @unittest.mock.patch("requests.get")
    def test_get_draft(self, mock_requests_get):
        mock_dict = {"foo": "bar"}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_draft(draft_id="12345")

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/draft/12345"
        )