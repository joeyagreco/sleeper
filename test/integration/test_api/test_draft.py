import unittest

from sleeper.api.draft import get_user_drafts_for_year
from sleeper.enum.Sport import Sport
from test.integration.test_api.constants import TEST_USER_ID


class TestDraft(unittest.TestCase):
    def test_get_user_drafts_for_year_happy_path(self):
        response = get_user_drafts_for_year(
            user_id=TEST_USER_ID, sport=Sport.NFL, year="2023"
        )

        self.assertEqual(4, len(response))
