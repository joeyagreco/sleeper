import os
import tempfile
import unittest
from unittest import mock

from requests import HTTPError

from sleeper.api.AvatarAPIClient import AvatarAPIClient
from sleeper.exception.SleeperAPIException import SleeperAPIException
from test.helper.helper_classes import MockResponse


class TestAvatarAPIClient(unittest.TestCase):
    PATH_TO_TEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files", "api"))

    @mock.patch("requests.get")
    def test_get_avatar_happy_path(self, mock_requests_get):
        mock_dict = {}
        with open(os.path.join(self.PATH_TO_TEST_DIR, "test.png"), "rb") as image:
            f = image.read()
            original_image_bytes = bytearray(f)
        mock_response = MockResponse(mock_dict, 200, content=original_image_bytes)
        mock_requests_get.return_value = mock_response

        with tempfile.TemporaryDirectory() as tempDir:
            fullImagePath = os.path.join(tempDir, "tmp.png")
            AvatarAPIClient.get_avatar(avatar_id="avatar_id", save_to_path=fullImagePath)

            with open(fullImagePath, "rb") as image:
                f = image.read()
                saved_image_bytes = bytearray(f)
            self.assertEqual(original_image_bytes, saved_image_bytes)
            self.assertTrue(os.path.exists(fullImagePath))

    @mock.patch("requests.get")
    def test_get_avatar_thumbnail_is_true_happy_path(self, mock_requests_get):
        mock_dict = {}
        with open(os.path.join(self.PATH_TO_TEST_DIR, "test.png"), "rb") as image:
            f = image.read()
            original_image_bytes = bytearray(f)
        mock_response = MockResponse(mock_dict, 200, content=original_image_bytes)
        mock_requests_get.return_value = mock_response

        with tempfile.TemporaryDirectory() as tempDir:
            fullImagePath = os.path.join(tempDir, "tmp.png")
            AvatarAPIClient.get_avatar(avatar_id="avatar_id", save_to_path=fullImagePath, thumbnail=True)

            with open(fullImagePath, "rb") as image:
                f = image.read()
                saved_image_bytes = bytearray(f)
            self.assertEqual(original_image_bytes, saved_image_bytes)
            self.assertTrue(os.path.exists(fullImagePath))

    @mock.patch("requests.get")
    def test_get_avatar_avatar_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(SleeperAPIException) as context:
            AvatarAPIClient.get_avatar(avatar_id="avatar_id", save_to_path="")
        self.assertEqual("No avatar found.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_avatar_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(HTTPError) as context:
            AvatarAPIClient.get_avatar(avatar_id="avatar_id", save_to_path="")
        self.assertEqual("404 Client Error", str(context.exception))
