from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.model.User import User


class UserAPIClient(SleeperAPIClient):
    @classmethod
    def get_user(cls, *, username: str = None, user_id: str = None) -> User:
        if username is None and user_id is None:
            raise ValueError("'username' and 'user_id' cannot both be None.")
        user_arg = username if username is not None else user_id
        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL, cls._VERSION, cls._USER_ROUTE, f"{user_arg}"
        )
        response_dict = cls._get(url)
        if response_dict is None:
            raise ValueError(f"Could not find User for username/user_id: '{user_arg}'.")
        return User.from_dict(response_dict)
