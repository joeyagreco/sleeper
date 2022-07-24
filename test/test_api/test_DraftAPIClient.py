import unittest
from unittest import mock

from sleeper import DraftAPIClient
from sleeper.enum.DraftStatus import DraftStatus
from sleeper.enum.DraftType import DraftType
from sleeper.enum.ScoringType import ScoringType
from sleeper.enum.SeasonType import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.exception.SleeperAPIException import SleeperAPIException
from sleeper.model.Draft import Draft
from sleeper.model.DraftMetadata import DraftMetadata
from sleeper.model.DraftSettings import DraftSettings
from test.helper.helper_classes import MockResponse


class TestDraftAPIClient(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_user_drafts_for_year_happy_path(self, mock_requests_get):
        mock_list = [
            {
                "type": "snake",
                "status": "complete",
                "start_time": 1630891562020,
                "sport": "nfl",
                "settings": {
                    "teams": 8,
                    "slots_wr": 3,
                    "slots_te": 1,
                    "slots_rb": 2,
                    "slots_qb": 2,
                    "slots_super_flex": 1,
                    "slots_flex": 3,
                    "slots_bn": 6,
                    "rounds": 17,
                    "reversal_round": 0,
                    "player_type": 0,
                    "pick_timer": 0,
                    "nomination_timer": 60,
                    "enforce_position_limits": 1,
                    "cpu_autopick": 1,
                    "alpha_sort": 0
                },
                "season_type": "regular",
                "season": "2021",
                "metadata": {
                    "scoring_type": "2qb",
                    "name": "The Test",
                    "description": "des"
                },
                "league_id": "738979251063275520",
                "last_picked": 1630897024291,
                "last_message_time": 1630897024793,
                "last_message_id": "740439424466202624",
                "draft_order": {"123": 45},
                "draft_id": "738979252392919040",
                "creators": ["12345", "67890"],
                "created": 1630548892636,
                "slot_to_roster_id": {"123": 45}
            }
        ]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = DraftAPIClient.get_user_drafts_for_year(user_id="user_id", sport=Sport.NFL, year="2020")

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Draft)
        self.assertEqual(1630548892636, response[0].created)
        self.assertEqual(["12345", "67890"], response[0].creators)
        self.assertEqual("738979252392919040", response[0].draft_id)
        self.assertEqual({"123": 45}, response[0].draft_order)
        self.assertEqual("740439424466202624", response[0].last_message_id)
        self.assertEqual(1630897024793, response[0].last_message_time)
        self.assertEqual(1630897024291, response[0].last_picked)
        self.assertEqual("738979251063275520", response[0].league_id)
        self.assertIsInstance(response[0].metadata, DraftMetadata)
        self.assertEqual("des", response[0].metadata.description)
        self.assertEqual("The Test", response[0].metadata.name)
        self.assertEqual(ScoringType.TWO_QB, response[0].metadata.scoring_type)
        self.assertEqual("2021", response[0].season)
        self.assertEqual(SeasonType.REGULAR, response[0].season_type)
        self.assertIsInstance(response[0].settings, DraftSettings)
        self.assertEqual(0, response[0].settings.alpha_sort)
        self.assertEqual(1, response[0].settings.cpu_autopick)
        self.assertEqual(1, response[0].settings.enforce_position_limits)
        self.assertEqual(60, response[0].settings.nomination_timer)
        self.assertEqual(0, response[0].settings.pick_timer)
        self.assertEqual(0, response[0].settings.player_type)
        self.assertEqual(0, response[0].settings.reversal_round)
        self.assertEqual(17, response[0].settings.rounds)
        self.assertEqual(6, response[0].settings.slots_bn)
        self.assertEqual(3, response[0].settings.slots_flex)
        self.assertEqual(2, response[0].settings.slots_qb)
        self.assertEqual(2, response[0].settings.slots_rb)
        self.assertEqual(1, response[0].settings.slots_super_flex)
        self.assertEqual(1, response[0].settings.slots_te)
        self.assertEqual(3, response[0].settings.slots_wr)
        self.assertEqual(8, response[0].settings.teams)
        self.assertEqual({"123": 45}, response[0].slot_to_roster_id)
        self.assertEqual(Sport.NFL, response[0].sport)
        self.assertEqual(1630891562020, response[0].start_time)
        self.assertEqual(DraftStatus.COMPLETE, response[0].status)
        self.assertEqual(DraftType.SNAKE, response[0].type)

    @mock.patch("requests.get")
    def test_get_user_drafts_for_year_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            DraftAPIClient.get_user_drafts_for_year(user_id="user_id", sport=Sport.NFL, year="2020")
        self.assertEqual("Could not get Drafts for user_id 'user_id', sport 'NFL', and year '2020'.",
                         str(context.exception))

    @mock.patch("requests.get")
    def test_get_user_drafts_for_year_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(SleeperAPIException) as context:
            DraftAPIClient.get_user_drafts_for_year(user_id="user_id", sport=Sport.NFL, year="2020")
        self.assertEqual("Got bad status code (404) from request.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_drafts_in_league_happy_path(self, mock_requests_get):
        mock_list = [
            {
                "type": "snake",
                "status": "complete",
                "start_time": 1630891562020,
                "sport": "nfl",
                "settings": {
                    "teams": 8,
                    "slots_wr": 3,
                    "slots_te": 1,
                    "slots_rb": 2,
                    "slots_qb": 2,
                    "slots_super_flex": 1,
                    "slots_flex": 3,
                    "slots_bn": 6,
                    "rounds": 17,
                    "reversal_round": 0,
                    "player_type": 0,
                    "pick_timer": 0,
                    "nomination_timer": 60,
                    "enforce_position_limits": 1,
                    "cpu_autopick": 1,
                    "alpha_sort": 0
                },
                "season_type": "regular",
                "season": "2021",
                "metadata": {
                    "scoring_type": "2qb",
                    "name": "The Test",
                    "description": "des"
                },
                "league_id": "738979251063275520",
                "last_picked": 1630897024291,
                "last_message_time": 1630897024793,
                "last_message_id": "740439424466202624",
                "draft_order": {"123": 45},
                "draft_id": "738979252392919040",
                "creators": ["12345", "67890"],
                "created": 1630548892636,
                "slot_to_roster_id": {"123": 45}
            }
        ]
        mock_response = MockResponse(mock_list, 200)
        mock_requests_get.return_value = mock_response

        response = DraftAPIClient.get_drafts_in_league(league_id="12345")

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Draft)
        self.assertEqual(1630548892636, response[0].created)
        self.assertEqual(["12345", "67890"], response[0].creators)
        self.assertEqual("738979252392919040", response[0].draft_id)
        self.assertEqual({"123": 45}, response[0].draft_order)
        self.assertEqual("740439424466202624", response[0].last_message_id)
        self.assertEqual(1630897024793, response[0].last_message_time)
        self.assertEqual(1630897024291, response[0].last_picked)
        self.assertEqual("738979251063275520", response[0].league_id)
        self.assertIsInstance(response[0].metadata, DraftMetadata)
        self.assertEqual("des", response[0].metadata.description)
        self.assertEqual("The Test", response[0].metadata.name)
        self.assertEqual(ScoringType.TWO_QB, response[0].metadata.scoring_type)
        self.assertEqual("2021", response[0].season)
        self.assertEqual(SeasonType.REGULAR, response[0].season_type)
        self.assertIsInstance(response[0].settings, DraftSettings)
        self.assertEqual(0, response[0].settings.alpha_sort)
        self.assertEqual(1, response[0].settings.cpu_autopick)
        self.assertEqual(1, response[0].settings.enforce_position_limits)
        self.assertEqual(60, response[0].settings.nomination_timer)
        self.assertEqual(0, response[0].settings.pick_timer)
        self.assertEqual(0, response[0].settings.player_type)
        self.assertEqual(0, response[0].settings.reversal_round)
        self.assertEqual(17, response[0].settings.rounds)
        self.assertEqual(6, response[0].settings.slots_bn)
        self.assertEqual(3, response[0].settings.slots_flex)
        self.assertEqual(2, response[0].settings.slots_qb)
        self.assertEqual(2, response[0].settings.slots_rb)
        self.assertEqual(1, response[0].settings.slots_super_flex)
        self.assertEqual(1, response[0].settings.slots_te)
        self.assertEqual(3, response[0].settings.slots_wr)
        self.assertEqual(8, response[0].settings.teams)
        self.assertEqual({"123": 45}, response[0].slot_to_roster_id)
        self.assertEqual(Sport.NFL, response[0].sport)
        self.assertEqual(1630891562020, response[0].start_time)
        self.assertEqual(DraftStatus.COMPLETE, response[0].status)
        self.assertEqual(DraftType.SNAKE, response[0].type)

    @mock.patch("requests.get")
    def test_get_drafts_in_league_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            DraftAPIClient.get_drafts_in_league(league_id="12345")
        self.assertEqual("Could not get Drafts for league_id '12345'.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_drafts_in_league_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(SleeperAPIException) as context:
            DraftAPIClient.get_drafts_in_league(league_id="12345")
        self.assertEqual("Got bad status code (404) from request.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_draft_happy_path(self, mock_requests_get):
        mock_dict = {
            "type": "snake",
            "status": "complete",
            "start_time": 1630891562020,
            "sport": "nfl",
            "settings": {
                "teams": 8,
                "slots_wr": 3,
                "slots_te": 1,
                "slots_rb": 2,
                "slots_qb": 2,
                "slots_super_flex": 1,
                "slots_flex": 3,
                "slots_bn": 6,
                "rounds": 17,
                "reversal_round": 0,
                "player_type": 0,
                "pick_timer": 0,
                "nomination_timer": 60,
                "enforce_position_limits": 1,
                "cpu_autopick": 1,
                "alpha_sort": 0
            },
            "season_type": "regular",
            "season": "2021",
            "metadata": {
                "scoring_type": "2qb",
                "name": "The Test",
                "description": "des"
            },
            "league_id": "738979251063275520",
            "last_picked": 1630897024291,
            "last_message_time": 1630897024793,
            "last_message_id": "740439424466202624",
            "draft_order": {"123": 45},
            "draft_id": "738979252392919040",
            "creators": ["12345", "67890"],
            "created": 1630548892636,
            "slot_to_roster_id": {"123": 45}
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = DraftAPIClient.get_draft(draft_id="12345")

        self.assertIsInstance(response, Draft)
        self.assertEqual(1630548892636, response.created)
        self.assertEqual(["12345", "67890"], response.creators)
        self.assertEqual("738979252392919040", response.draft_id)
        self.assertEqual({"123": 45}, response.draft_order)
        self.assertEqual("740439424466202624", response.last_message_id)
        self.assertEqual(1630897024793, response.last_message_time)
        self.assertEqual(1630897024291, response.last_picked)
        self.assertEqual("738979251063275520", response.league_id)
        self.assertIsInstance(response.metadata, DraftMetadata)
        self.assertEqual("des", response.metadata.description)
        self.assertEqual("The Test", response.metadata.name)
        self.assertEqual(ScoringType.TWO_QB, response.metadata.scoring_type)
        self.assertEqual("2021", response.season)
        self.assertEqual(SeasonType.REGULAR, response.season_type)
        self.assertIsInstance(response.settings, DraftSettings)
        self.assertEqual(0, response.settings.alpha_sort)
        self.assertEqual(1, response.settings.cpu_autopick)
        self.assertEqual(1, response.settings.enforce_position_limits)
        self.assertEqual(60, response.settings.nomination_timer)
        self.assertEqual(0, response.settings.pick_timer)
        self.assertEqual(0, response.settings.player_type)
        self.assertEqual(0, response.settings.reversal_round)
        self.assertEqual(17, response.settings.rounds)
        self.assertEqual(6, response.settings.slots_bn)
        self.assertEqual(3, response.settings.slots_flex)
        self.assertEqual(2, response.settings.slots_qb)
        self.assertEqual(2, response.settings.slots_rb)
        self.assertEqual(1, response.settings.slots_super_flex)
        self.assertEqual(1, response.settings.slots_te)
        self.assertEqual(3, response.settings.slots_wr)
        self.assertEqual(8, response.settings.teams)
        self.assertEqual({"123": 45}, response.slot_to_roster_id)
        self.assertEqual(Sport.NFL, response.sport)
        self.assertEqual(1630891562020, response.start_time)
        self.assertEqual(DraftStatus.COMPLETE, response.status)
        self.assertEqual(DraftType.SNAKE, response.type)
