import unittest

from sleeper.api.draft import get_user_drafts_for_year
from sleeper.enum.Sport import Sport
from test.helper.helper_classes import MockResponse


class TestDraftAPIClient(unittest.TestCase):
    @unittest.mock.patch("requests.get")
    def test_get_user_drafts_for_year_happy_path(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_user_drafts_for_year(
            user_id="user_id", sport=Sport.NFL, year="2020"
        )

        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
