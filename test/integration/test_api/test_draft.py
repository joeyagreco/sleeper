import unittest

from sleeper.api import (
    get_draft,
    get_drafts_in_league,
    get_player_draft_picks,
    get_traded_draft_picks,
    get_user_drafts_for_year,
)
from test.integration.test_api.constants import (
    LEAGUE_A_DRAFT_1,
    LEAGUE_A_DRAFT_ID_1,
    LEAGUE_A_DRAFT_ID_2,
    LEAGUE_A_DRAFT_ID_2_TRADED_PICKS,
    LEAGUE_A_DRAFTS,
    LEAGUE_A_LEAGUE_ID,
    USER_A_DRAFT_PICKS_DRAFT_ID_1_2023,
    USER_A_DRAFTS_2023,
    USER_A_USER_ID,
)


class TestDraft(unittest.TestCase):
    def test_get_user_drafts_for_year_happy_path(self):
        response = get_user_drafts_for_year(
            user_id=USER_A_USER_ID, sport="nfl", year=2023
        )
        self.assertEqual(USER_A_DRAFTS_2023, response)

    def test_get_drafts_in_league(self):
        response = get_drafts_in_league(league_id=LEAGUE_A_LEAGUE_ID)
        self.assertEqual(LEAGUE_A_DRAFTS, response)

    def test_get_draft(self):
        response = get_draft(draft_id=LEAGUE_A_DRAFT_ID_1)
        self.assertEqual(LEAGUE_A_DRAFT_1, response)

    def test_get_player_draft_picks(self):
        response = get_player_draft_picks(
            draft_id=LEAGUE_A_DRAFT_ID_1,
        )
        self.assertEqual(USER_A_DRAFT_PICKS_DRAFT_ID_1_2023, response)

    def test_get_traded_draft_picks(self):
        response = get_traded_draft_picks(draft_id=LEAGUE_A_DRAFT_ID_2)
        self.assertEqual(LEAGUE_A_DRAFT_ID_2_TRADED_PICKS, response)
