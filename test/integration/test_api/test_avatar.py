import os
import unittest

from sleeper.api import get_avatar
from test.integration.test_api.constants import USER_B_AVATAR_ID


class TestAvatar(unittest.TestCase):
    _PATH_TO_TEST_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "util", "bin")
    )

    with open(os.path.join(_PATH_TO_TEST_DIR, "sleeper.bin"), "rb") as image:
        _SLEEPER_AVATAR_BYTES = image.read()

    with open(os.path.join(_PATH_TO_TEST_DIR, "sleeper_thumb.bin"), "rb") as image:
        _SLEEPER_THUMBNAIL_AVATAR_BYTES = image.read()

    def test_get_avatar_defaults(self):
        response = get_avatar(avatar_id=USER_B_AVATAR_ID)
        self.assertEqual(self._SLEEPER_AVATAR_BYTES, response)

    def test_get_avatar_as_thumbnail(self):
        response = get_avatar(avatar_id=USER_B_AVATAR_ID, as_thumbnail=True)
        self.assertEqual(self._SLEEPER_THUMBNAIL_AVATAR_BYTES, response)
