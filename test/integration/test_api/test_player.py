import unittest

from sleeper.api import get_all_players, get_trending_players


class TestPlayer(unittest.TestCase):
    def test_get_all_players(self):
        response = get_all_players(sport="nfl")
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, dict)
        for k, v in response.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, dict)

    def test_get_trending_players(self):
        response = get_trending_players(sport="nfl", trend_type="add")
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, list)
        self.assertEqual(25, len(response))
        for item in response:
            self.assertIsInstance(item, dict)
