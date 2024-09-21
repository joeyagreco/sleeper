from sleeper.api._constants import SLEEPER_APP_BASE_URL, USER_ROUTE, VERSION
from sleeper.api._utils import build_route, get


def get_user(*, identifier: str) -> dict:
    # identifier can be username or user id
    return get(build_route(SLEEPER_APP_BASE_URL, VERSION, USER_ROUTE, f"{identifier}"))
