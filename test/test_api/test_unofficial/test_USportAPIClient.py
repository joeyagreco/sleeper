import datetime
import unittest
from test.helper.helper_classes import MockResponse
from unittest import mock

from sleeper.api.unofficial import USportAPIClient
from sleeper.enum import SeasonStatus
from sleeper.enum.nfl import NFLTeam
from sleeper.enum.Sport import Sport
from sleeper.model import Game


class TestUSportAPIClient(unittest.TestCase):
    @mock.patch("requests.get")
    def test_get_player_stats_no_week_given_happy_path(self, mock_requests_get):
        mock_list = [
            {
                "week": 1,
                "status": "complete",
                "home": "ATL",
                "game_id": "1234",
                "date": "2021-09-12",
                "away": "PHI",
            }
        ]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = USportAPIClient.get_regular_season_schedule(sport=Sport.NFL, season="2021")

        self.assertIsInstance(response, list)
        self.assertEqual(1, len(response))
        self.assertIsInstance(response[0], Game)
        self.assertEqual(1, response[0].week)
        self.assertEqual(SeasonStatus.COMPLETE, response[0].status)
        self.assertEqual(NFLTeam.ATL, response[0].home)
        self.assertEqual("1234", response[0].game_id)
        self.assertEqual(datetime.datetime(2021, 9, 12).date(), response[0].date)
        self.assertEqual(NFLTeam.PHI, response[0].away)
