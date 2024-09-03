import unittest

from sleeper.api.player import get_all_players
from sleeper.enum.Sport import Sport
from test.unit.helper.helper_classes import MockResponse


class TestPlayer(unittest.TestCase):
    @unittest.mock.patch("requests.get")
    def test_get_all_players(self, mock_requests_get):
        mock_dict = {"foo": {"bar": "baz"}}
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = get_all_players(sport=Sport.NFL)

        self.assertEqual(mock_dict, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/players/nfl"
        )
