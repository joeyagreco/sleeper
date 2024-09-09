from sleeper.api.constants import SLEEPER_APP_BASE_URL, USER_ROUTE, VERSION
from sleeper.api.util import build_route, get


def get_user(*, user_identifier: str) -> dict:
    # user_identifier can be username or user_id
    url = build_route(SLEEPER_APP_BASE_URL, VERSION, USER_ROUTE, f"{user_identifier}")
    response_dict = get(url)
    if response_dict is None:
        raise ValueError(
            f"Could not find User for username/user_id: '{user_identifier}'."
        )
    return response_dict
