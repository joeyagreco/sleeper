from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class User:
    username: Optional[str]
    user_id: str
    display_name: str
    avatar: str
    league_id: Optional[str]
    is_owner: Optional[bool]
    is_bot: Optional[bool]

    @staticmethod
    def from_dict(user_dict: dict) -> User:
        return User(username=user_dict.get("username", None),
                    user_id=user_dict["user_id"],
                    display_name=user_dict["display_name"],
                    avatar=user_dict["avatar"],
                    is_owner=user_dict.get("is_owner", False),
                    is_bot=user_dict.get("is_bot", False),
                    league_id=user_dict.get("league_id", None))

    @staticmethod
    def from_dict_list(user_dict_list: dict) -> list[User]:
        users = list()
        for user_dict in user_dict_list:
            users.append(User.from_dict(user_dict))
        return users
