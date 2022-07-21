import unittest
from unittest import mock

from sleeper.api.UserAPIClient import UserAPIClient
from sleeper.model.User import User


class MockResponse:
    def __init__(self, data: dict, status_code: int):
        self.__data = data
        self.__status_code = status_code

    def json(self):
        return self.__data


class TestUserAPIClient(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_user_happy_path(self, mock_requests_get):
        mock_dict = {
            "verification": None,
            "username": "username",
            "user_id": "user_id",
            "token": None,
            "summoner_region": None,
            "solicitable": None,
            "real_name": None,
            "phone": None,
            "pending": None,
            "notifications": None,
            "metadata": None,
            "is_bot": True,
            "email": None,
            "display_name": "display_name",
            "deleted": None,
            "data_updated": None,
            "currencies": None,
            "created": None,
            "cookies": None,
            "avatar": "avatar"
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UserAPIClient.get_user(user_id="user_id")

        self.assertIsInstance(response, User)
        self.assertEqual(response.username, "username")
        self.assertEqual(response.user_id, "user_id")
        self.assertEqual(response.display_name, "display_name")
        self.assertEqual(response.avatar, "avatar")
