from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class User:
    avatar: str
    cookies: Any  # not sure what this is
    created: Any  # not sure what this is
    currencies: Any  # not sure what this is
    data_updated: Any  # not sure what this is
    deleted: Any  # not sure what this is
    display_name: str
    email: str
    is_bot: bool
    is_owner: bool
    league_id: str
    metadata: Any  # not sure what this is
    notifications: Any  # not sure what this is
    pending: Any  # not sure what this is
    phone: str
    real_name: str
    solicitable: Any  # not sure what this is
    summoner_region: Any  # not sure what this is
    token: str
    user_id: str
    username: str
    verification: Any  # not sure what this is

    @staticmethod
    def from_dict(user_dict: dict) -> User:
        return User(
            username=user_dict.get("username"),
            user_id=user_dict.get("user_id"),
            display_name=user_dict.get("display_name"),
            avatar=user_dict.get("avatar"),
            is_owner=user_dict.get("is_owner", False),
            is_bot=user_dict.get("is_bot", False),
            league_id=user_dict.get("league_id"),
            cookies=user_dict.get("cookies"),
            created=user_dict.get("created"),
            currencies=user_dict.get("currencies"),
            data_updated=user_dict.get("data_updated"),
            deleted=user_dict.get("deleted"),
            email=user_dict.get("email"),
            metadata=user_dict.get("metadata"),
            notifications=user_dict.get("notifications"),
            pending=user_dict.get("pending"),
            phone=user_dict.get("phone"),
            real_name=user_dict.get("real_name"),
            solicitable=user_dict.get("solicitable"),
            summoner_region=user_dict.get("summoner_region"),
            token=user_dict.get("token"),
            verification=user_dict.get("verification"),
        )

    @staticmethod
    def from_dict_list(user_dict_list: list) -> list[User]:
        users = list()
        for user_dict in user_dict_list:
            users.append(User.from_dict(user_dict))
        return users
