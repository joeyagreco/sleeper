import unittest
from unittest import mock

from sleeper.api.PlayerAPIClient import PlayerAPIClient
from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.PracticeParticipation import PracticeParticipation
from sleeper.enum.Sport import Sport
from sleeper.enum.nfl.NFLPlayerStatus import NFLPlayerStatus
from sleeper.enum.nfl.NFLPosition import NFLPosition
from sleeper.enum.nfl.NFLTeam import NFLTeam


class MockResponse:
    def __init__(self, data: dict, status_code: int, **kwargs):
        self.__data = data
        self.content = kwargs.pop("content", None)
        self.status_code = status_code

    def json(self):
        return self.__data


class TestPlayerAPIClient(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_all_players_happy_path(self, mock_requests_get):
        mock_dict = {
            "2103": {
                "player_id": "2103",
                "number": 60,
                "years_exp": 1,
                "swish_id": None,
                "birth_city": None,
                "espn_id": 17054,
                "rotowire_id": 9866,
                "injury_notes": None,
                "gsis_id": None,
                "birth_state": None,
                "weight": "285",
                "status": "Inactive",
                "practice_description": None,
                "last_name": "Booth",
                "hashtag": "#codybooth-NFL-FA-60",
                "fantasy_positions": [
                    "OL"
                ],
                "position": "OT",
                "stats_id": 12345,
                "search_last_name": "booth",
                "yahoo_id": 27841,
                "birth_country": "USA",
                "full_name": "Cody Booth",
                "age": 27,
                "sport": "nfl",
                "team": "GB",
                "pandascore_id": None,
                "high_school": None,
                "news_updated": None,
                "metadata": None,
                "injury_body_part": None,
                "injury_start_date": "20000101",
                "fantasy_data_id": 16426,
                "depth_chart_position": 1,
                "height": "6'5\"",
                "injury_status": None,
                "sportradar_id": "4cd4976e-e230-4935-ad3f-c12876a41350",
                "practice_participation": None,
                "birth_date": "1991-04-22",
                "first_name": "Cody",
                "active": False,
                "depth_chart_order": 1,
                "college": "Temple",
                "rotoworld_id": 12345,
                "search_rank": 9999999,
                "search_first_name": "cody",
                "search_full_name": "codybooth"
            }
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = PlayerAPIClient.get_all_players(sport=Sport.NFL)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual(27, response["2103"].age)
        self.assertEqual("USA", response["2103"].birth_country)
        self.assertEqual("Temple", response["2103"].college)
        self.assertEqual(1, response["2103"].depth_chart_order)
        self.assertEqual(1, response["2103"].depth_chart_position)
        self.assertEqual(17054, response["2103"].espn_id)
        self.assertEqual(16426, response["2103"].fantasy_data_id)
        self.assertEqual(1, len(response["2103"].fantasy_positions))
        self.assertEqual(NFLPosition.OL, response["2103"].fantasy_positions[0])
        self.assertEqual("Cody", response["2103"].first_name)
        self.assertEqual("#codybooth-NFL-FA-60", response["2103"].hashtag)
        self.assertEqual("6'5\"", response["2103"].height)
        self.assertEqual("20000101", response["2103"].injury_start_date)
        self.assertEqual(InjuryStatus.NA, response["2103"].injury_status)
        self.assertEqual("Booth", response["2103"].last_name)
        self.assertEqual(60, response["2103"].number)
        self.assertEqual("2103", response["2103"].player_id)
        self.assertEqual(NFLPosition.OT, response["2103"].position)
        self.assertEqual(PracticeParticipation.NA, response["2103"].practice_participation)
        self.assertEqual(9866, response["2103"].rotowire_id)
        self.assertEqual(12345, response["2103"].rotoworld_id)
        self.assertEqual("cody", response["2103"].search_first_name)
        self.assertEqual("codybooth", response["2103"].search_full_name)
        self.assertEqual("booth", response["2103"].search_last_name)
        self.assertEqual(9999999, response["2103"].search_rank)
        self.assertEqual(Sport.NFL, response["2103"].sport)
        self.assertEqual("4cd4976e-e230-4935-ad3f-c12876a41350", response["2103"].sportradar_id)
        self.assertEqual(12345, response["2103"].stats_id)
        self.assertEqual(NFLPlayerStatus.INACTIVE, response["2103"].status)
        self.assertEqual(NFLTeam.GB, response["2103"].team)
        self.assertEqual("285", response["2103"].weight)
        self.assertEqual(27841, response["2103"].yahoo_id)
        self.assertEqual(1, response["2103"].years_exp)
