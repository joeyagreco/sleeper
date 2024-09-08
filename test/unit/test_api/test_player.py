import unittest

from sleeper.api.player import get_all_players, get_trending_players
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType
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

    @unittest.mock.patch("requests.get")
    def test_get_trending_players_with_defaults(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_trending_players(sport=Sport.NFL, trend_type=TrendType.ADD)

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/players/nfl/trending/add"
        )

    @unittest.mock.patch("requests.get")
    def test_get_trending_players_with_optional_params_given(self, mock_requests_get):
        mock_list = [{"foo": "bar"}]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = get_trending_players(
            sport=Sport.NFL, trend_type=TrendType.ADD, lookback_hours=1, limit=2
        )

        self.assertEqual(mock_list, response)
        mock_requests_get.assert_called_once_with(
            "https://api.sleeper.app/v1/players/nfl/trending/add?lookback_hours=1&limit=2"
        )
