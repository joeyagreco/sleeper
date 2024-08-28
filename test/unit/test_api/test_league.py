import unittest

from sleeper.api.league import get_league
from test.unit.helper.helper_classes import MockResponse


class TestLeague(unittest.TestCase):
    @unittest.mock.patch("requests.get")
    def test_get_league(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_league(league_id="12345")

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/league/12345"
        )
