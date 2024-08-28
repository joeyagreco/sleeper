import unittest

from sleeper.api.draft import get_drafts_in_league, get_user_drafts_for_year
from sleeper.enum.Sport import Sport
from test.integration.test_api.constants import (
    TEST_DRAFTS_FOR_LEAGUE_A,
    TEST_DRAFTS_FOR_USER_A,
    TEST_LEAGUE_ID_FOR_LEAGUE_A,
    TEST_USER_ID_FOR_USER_A,
)


class TestDraft(unittest.TestCase):
    def test_get_user_drafts_for_year_happy_path(self):
        response = get_user_drafts_for_year(
            user_id=TEST_USER_ID_FOR_USER_A, sport=Sport.NFL, year="2023"
        )
        self.assertEqual(TEST_DRAFTS_FOR_USER_A, response)

    def test_get_drafts_in_league(self):
        response = get_drafts_in_league(league_id=TEST_LEAGUE_ID_FOR_LEAGUE_A)
        self.assertEqual(TEST_DRAFTS_FOR_LEAGUE_A, response)
