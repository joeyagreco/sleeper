import unittest

from sleeper.api.league import get_league
from test.integration.test_api.constants import TEST_LEAGUE_ID, TEST_LEAGUE_OBJECT


class TestLeague(unittest.TestCase):
    def test_get_league(self):
        response = get_league(league_id=TEST_LEAGUE_ID)
        self.assertEqual(TEST_LEAGUE_OBJECT, response)
