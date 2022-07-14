from sleeper.api.APIClient import APIClient
from sleeper.model.User import User
from sleeper.util.ConfigReader import ConfigReader


class UserAPIClient(APIClient):
    __USER_ROUTE = ConfigReader.get("api", "user_route")
    __USERS_ROUTE = ConfigReader.get("api", "users_route")
    __LEAGUE_ROUTE = ConfigReader.get("api", "league_route")

    @staticmethod
    def __build_user_object(user_dict: dict) -> User:
        return User(username=user_dict.get("username", None),
                    user_id=user_dict["user_id"],
                    display_name=user_dict["display_name"],
                    avatar=user_dict["avatar"],
                    is_owner=user_dict.get("is_owner", False),
                    is_bot=user_dict.get("is_bot", False),
                    league_id=user_dict.get("league_id", None))

    @classmethod
    def __build_users_list(cls, user_dict_list: dict) -> list[User]:
        users = list()
        for user_dict in user_dict_list:
            users.append(cls.__build_user_object(user_dict))
        return users

    @classmethod
    def get_user(cls, *, username: str = None, user_id: str = None) -> User:
        if username is None and user_id is None:
            raise ValueError("Must pass 'username' or 'user_id'.")
        user_arg = username if username is not None else user_id
        url = cls._build_route(cls.__USER_ROUTE, f"{user_arg}")
        return cls.__build_user_object(cls._get(url))

    @classmethod
    def get_users_in_league(cls, *, league_id: str) -> list[User]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__USERS_ROUTE)
        return cls.__build_users_list(cls._get(url))
