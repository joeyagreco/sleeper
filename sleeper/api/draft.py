from sleeper.api.constants import (
    DRAFTS_ROUTE,
    SLEEPER_APP_BASE_URL,
    USER_ROUTE,
    VERSION,
)
from sleeper.api.util import build_route, get
from sleeper.enum.Sport import Sport


def get_user_drafts_for_year(*, user_id: str, sport: Sport, year: str) -> dict:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        USER_ROUTE,
        user_id,
        DRAFTS_ROUTE,
        sport.name.lower(),
        year,
    )
    response_list = get(url)
    if response_list is None:
        raise ValueError(
            f"Could not get Drafts for user_id '{user_id}', sport '{sport.name}', and year '{year}'."
        )
    return response_list
