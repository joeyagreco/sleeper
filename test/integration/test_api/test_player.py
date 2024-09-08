import unittest

from sleeper.api.player import get_all_players, get_trending_players
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType


class TestPlayer(unittest.TestCase):
    def test_get_all_players(self):
        response = get_all_players(sport=Sport.NFL)
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, dict)
        for k, v in response.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, dict)

    def test_get_trending_players(self):
        response = get_trending_players(sport=Sport.NFL, trend_type=TrendType.ADD)
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, list)
        self.assertEqual(25, len(response))
        for item in response:
            self.assertIsInstance(item, dict)
