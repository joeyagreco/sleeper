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
