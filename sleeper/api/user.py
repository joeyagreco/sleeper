from sleeper.api._constants import SLEEPER_APP_BASE_URL, USER_ROUTE, VERSION
from sleeper.api._utils import build_route, get


def get_user(*, user_identifier: str) -> dict:
    # user_identifier can be username or user_id
    url = build_route(SLEEPER_APP_BASE_URL, VERSION, USER_ROUTE, f"{user_identifier}")
    return get(url)
