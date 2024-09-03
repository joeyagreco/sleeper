import unittest

from sleeper.api.player import get_all_players
from sleeper.enum.Sport import Sport


class TestPlayer(unittest.TestCase):
    def test_get_all_players(self):
        response = get_all_players(sport=Sport.NFL)
        # this response will constantly change, so just assert some general things
        self.assertIsInstance(response, dict)
        for k, v in response.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, dict)
