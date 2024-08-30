import unittest

from sleeper.api.draft import get_draft, get_drafts_in_league, get_user_drafts_for_year
from sleeper.enum.Sport import Sport
from test.integration.test_api.constants import (
    LEAGUE_A_DRAFT_1,
    LEAGUE_A_DRAFT_ID_1,
    LEAGUE_A_DRAFTS,
    LEAGUE_A_LEAGUE_ID_1,
    USER_A_DRAFTS_2023,
    USER_A_USER_ID,
)


class TestDraft(unittest.TestCase):
    def test_get_user_drafts_for_year_happy_path(self):
        response = get_user_drafts_for_year(
            user_id=USER_A_USER_ID, sport=Sport.NFL, year="2023"
        )
        self.assertEqual(USER_A_DRAFTS_2023, response)

    def test_get_drafts_in_league(self):
        response = get_drafts_in_league(league_id=LEAGUE_A_LEAGUE_ID_1)
        self.assertEqual(LEAGUE_A_DRAFTS, response)

    def test_get_draft(self):
        response = get_draft(draft_id=LEAGUE_A_DRAFT_ID_1)
        self.assertEqual(LEAGUE_A_DRAFT_1, response)
