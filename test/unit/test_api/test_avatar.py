import unittest
from unittest.mock import patch

from sleeper.api import get_avatar
from test.unit.helper.helper_classes import MockResponse


class TestAvatar(unittest.TestCase):
    @patch("requests.get")
    def test_get_avatar_defaults(self, mock_requests_get):
        mock_bytes = b"foo"
        mock_response = MockResponse({}, 200, mock_bytes)
        mock_requests_get.return_value = mock_response

        response = get_avatar(avatar_id="abc")

        self.assertEqual(mock_bytes, response)
        mock_requests_get.assert_called_once_with("https://sleepercdn.com/avatars/abc")

    @patch("requests.get")
    def test_get_avatar_as_thumbnail(self, mock_requests_get):
        mock_bytes = b"foo"
        mock_response = MockResponse({}, 200, mock_bytes)
        mock_requests_get.return_value = mock_response

        response = get_avatar(avatar_id="abc", as_thumbnail=True)

        self.assertEqual(mock_bytes, response)
        mock_requests_get.assert_called_once_with(
            "https://sleepercdn.com/avatars/thumbs/abc"
        )
