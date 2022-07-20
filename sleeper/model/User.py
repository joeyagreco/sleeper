from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class User:
    avatar: str
    display_name: str
    is_bot: bool
    is_owner: bool
    league_id: str
    user_id: str
    username: str

    @staticmethod
    def from_dict(user_dict: dict) -> User:
        return User(username=user_dict.get("username"),
                    user_id=user_dict.get("user_id"),
                    display_name=user_dict.get("display_name"),
                    avatar=user_dict.get("avatar"),
                    is_owner=user_dict.get("is_owner", False),
                    is_bot=user_dict.get("is_bot", False),
                    league_id=user_dict.get("league_id"))

    @staticmethod
    def from_dict_list(user_dict_list: dict) -> list[User]:
        users = list()
        for user_dict in user_dict_list:
            users.append(User.from_dict(user_dict))
        return users
