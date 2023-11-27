import unittest
from test.helper.helper_classes import MockResponse
from unittest import mock

from requests import HTTPError

from sleeper.api.UserAPIClient import UserAPIClient
from sleeper.model.User import User


class TestUserAPIClient(unittest.TestCase):
    @mock.patch("requests.get")
    def test_get_user_happy_path(self, mock_requests_get):
        mock_dict = {
            "verification": "v",
            "username": "username",
            "user_id": "user_id",
            "token": "t",
            "summoner_region": "r",
            "solicitable": "s",
            "real_name": "name",
            "phone": "1",
            "pending": "1",
            "notifications": "1",
            "metadata": {"test": "t"},
            "is_bot": True,
            "email": "email",
            "display_name": "display_name",
            "deleted": "deleted",
            "data_updated": "data",
            "currencies": "currencies",
            "created": "created",
            "cookies": "cookies",
            "avatar": "avatar",
        }
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        response = UserAPIClient.get_user(user_id="user_id")

        self.assertIsInstance(response, User)
        self.assertEqual(response.username, "username")
        self.assertEqual(response.user_id, "user_id")
        self.assertEqual(response.display_name, "display_name")
        self.assertEqual(response.avatar, "avatar")
        self.assertEqual("cookies", response.cookies)
        self.assertEqual("created", response.created)
        self.assertEqual("currencies", response.currencies)
        self.assertEqual("data", response.data_updated)
        self.assertEqual("deleted", response.deleted)
        self.assertEqual("email", response.email)
        self.assertEqual({"test": "t"}, response.metadata)
        self.assertEqual("1", response.notifications)
        self.assertEqual("1", response.pending)
        self.assertEqual("1", response.phone)
        self.assertEqual("name", response.real_name)
        self.assertEqual("s", response.solicitable)
        self.assertEqual("r", response.summoner_region)
        self.assertEqual("t", response.token)
        self.assertEqual("v", response.verification)

    def test_get_user_username_and_user_id_not_given_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            UserAPIClient.get_user()
        self.assertEqual("'username' and 'user_id' cannot both be None.", str(context.exception))

    @mock.patch("requests.get")
    def test_get_user_username_or_user_id_not_found_raises_exception(self, mock_requests_get):
        mock_dict = None
        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            UserAPIClient.get_user(user_id="user_id")
        self.assertEqual(
            "Could not find User for username/user_id: 'user_id'.", str(context.exception)
        )

    @mock.patch("requests.get")
    def test_get_user_non_200_status_code_raises_exception(self, mock_requests_get):
        mock_dict = {}
        mock_response = MockResponse(mock_dict, 404)
        mock_requests_get.return_value = mock_response

        with self.assertRaises(HTTPError) as context:
            UserAPIClient.get_user(user_id="user_id")
        self.assertEqual("404 Client Error", str(context.exception))
