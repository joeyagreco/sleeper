import unittest

from sleeper.api.league import get_league, get_rosters, get_user_leagues_for_year
from sleeper.enum import Sport
from test.integration.test_api.constants import (
    LEAGUE_A_LEAGUE_1,
    LEAGUE_A_LEAGUE_ID_1,
    USER_A_LEAGUES_2022,
    USER_A_USER_ID,
)


class TestLeague(unittest.TestCase):
    def test_get_league(self):
        response = get_league(league_id=LEAGUE_A_LEAGUE_ID_1)
        self.assertEqual(LEAGUE_A_LEAGUE_1, response)

    def test_get_user_leagues_for_year(self):
        response = get_user_leagues_for_year(
            user_id=USER_A_USER_ID, sport=Sport.NFL, year=2022
        )
        self.assertEqual(USER_A_LEAGUES_2022, response)

    def test_get_rosters(self):
        response = get_rosters(league_id=LEAGUE_A_LEAGUE_ID_1)
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, list)
        self.assertEqual(6, len(response))
        for item in response:
            self.assertIsInstance(item, dict)
