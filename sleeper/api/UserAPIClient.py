from sleeper.api.APIClient import APIClient
from sleeper.model.User import User
from sleeper.util.ConfigReader import ConfigReader


class UserAPIClient(APIClient):

    def __init__(self, *, username: str = None, user_id: str = None):
        if username is None and user_id is None:
            raise ValueError("Must pass 'username' or 'user_id'.")
        self.__username = username
        self.__user_id = user_id

        self.__USER_ROUTE = ConfigReader.get("api", "user_route")

    @staticmethod
    def __build_user_object(user_dict: dict) -> User:
        return User(username=user_dict["username"],
                    user_id=user_dict["user_id"],
                    display_name=user_dict["display_name"],
                    avatar=user_dict["avatar"])

    def get_user(self) -> User:
        user_arg = self.__username if self.__username is not None else self.__user_id
        url = self._build_route(self.__USER_ROUTE, f"{user_arg}")
        return self.__build_user_object(self._get(url))
