import unittest

from sleeper.api import (
    get_league,
    get_losers_bracket,
    get_matchups_for_week,
    get_rosters,
    get_sport_state,
    get_traded_picks,
    get_transactions,
    get_user_leagues_for_year,
    get_users_in_league,
    get_winners_bracket,
)
from test.integration.test_api.constants import (
    LEAGUE_A_LEAGUE,
    LEAGUE_A_LEAGUE_ID,
    LEAGUE_B_LEAGUE_ID,
    LEAGUE_B_LOSERS_BRACKET,
    LEAGUE_B_USERS,
    LEAGUE_B_WEEK_1_MATCHUPS,
    LEAGUE_B_WEEK_1_TRANSACTIONS,
    LEAGUE_B_WINNERS_BRACKET,
    LEAGUE_C_LEAGUE_ID,
    LEAGUE_C_TRADED_PICKS,
    USER_A_LEAGUES_2022,
    USER_A_USER_ID,
)


class TestLeague(unittest.TestCase):
    def test_get_league(self):
        response = get_league(league_id=LEAGUE_A_LEAGUE_ID)
        self.assertEqual(LEAGUE_A_LEAGUE, response)

    def test_get_user_leagues_for_year(self):
        response = get_user_leagues_for_year(
            user_id=USER_A_USER_ID, sport="nfl", year=2022
        )
        self.assertEqual(USER_A_LEAGUES_2022, response)

    def test_get_rosters(self):
        response = get_rosters(league_id=LEAGUE_A_LEAGUE_ID)
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, list)
        self.assertEqual(6, len(response))
        for item in response:
            self.assertIsInstance(item, dict)

    def test_get_users_in_league(self):
        response = get_users_in_league(league_id=LEAGUE_B_LEAGUE_ID)
        self.assertEqual(LEAGUE_B_USERS, response)

    def test_get_matchups_for_week(self):
        response = get_matchups_for_week(league_id=LEAGUE_B_LEAGUE_ID, week=1)
        self.assertEqual(LEAGUE_B_WEEK_1_MATCHUPS, response)

    def test_get_winners_bracket(self):
        response = get_winners_bracket(league_id=LEAGUE_B_LEAGUE_ID)
        self.assertEqual(LEAGUE_B_WINNERS_BRACKET, response)

    def test_get_losers_bracket(self):
        response = get_losers_bracket(league_id=LEAGUE_B_LEAGUE_ID)
        self.assertEqual(LEAGUE_B_LOSERS_BRACKET, response)

    def test_get_transactions(self):
        response = get_transactions(league_id=LEAGUE_B_LEAGUE_ID, week=1)
        self.assertEqual(LEAGUE_B_WEEK_1_TRANSACTIONS, response)

    def test_get_traded_picks(self):
        response = get_traded_picks(league_id=LEAGUE_C_LEAGUE_ID)
        self.assertEqual(LEAGUE_C_TRADED_PICKS, response)

    def test_get_sport_state(self):
        response = get_sport_state(sport="nfl")
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, dict)
        for k in response.keys():
            self.assertIsInstance(k, str)
