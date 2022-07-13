from dataclasses import dataclass


@dataclass(kw_only=True)
class User:
    username: str
    user_id: str
    display_name: str
    avatar: str
