import unittest

from sleeper.api.league import get_league
from test.integration.test_api.constants import (
    LEAGUE_A_LEAGUE_1,
    LEAGUE_A_LEAGUE_ID_1,
)


class TestLeague(unittest.TestCase):
    def test_get_league(self):
        response = get_league(league_id=LEAGUE_A_LEAGUE_ID_1)
        self.assertEqual(LEAGUE_A_LEAGUE_1, response)
