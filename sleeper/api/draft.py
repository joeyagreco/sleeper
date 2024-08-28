from sleeper.api.constants import (
    DRAFT_ROUTE,
    DRAFTS_ROUTE,
    LEAGUE_ROUTE,
    SLEEPER_APP_BASE_URL,
    USER_ROUTE,
    VERSION,
)
from sleeper.api.util import build_route, get
from sleeper.enum.Sport import Sport


def get_user_drafts_for_year(*, user_id: str, sport: Sport, year: str) -> list[dict]:
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


def get_drafts_in_league(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        DRAFTS_ROUTE,
    )
    response_list = get(url)
    if response_list is None:
        raise ValueError(f"Could not get Drafts for league_id '{league_id}'.")
    return response_list


def get_draft(*, draft_id: str) -> dict:
    url = build_route(SLEEPER_APP_BASE_URL, VERSION, DRAFT_ROUTE, draft_id)
    response_dict = get(url)
    if response_dict is None:
        raise ValueError(f"Could not get Draft with draft_id '{draft_id}'.")
    return response_dict
