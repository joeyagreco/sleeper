from sleeper.api.constants import (
    LEAGUE_ROUTE,
    LEAGUES_ROUTE,
    MATCHUPS_ROUTE,
    ROSTERS_ROUTE,
    SLEEPER_APP_BASE_URL,
    USER_ROUTE,
    USERS_ROUTE,
    VERSION,
)
from sleeper.api.util import build_route, get
from sleeper.enum import Sport


def get_league(*, league_id: str) -> dict:
    url = build_route(SLEEPER_APP_BASE_URL, VERSION, LEAGUE_ROUTE, league_id)
    return get(url)


def get_user_leagues_for_year(*, user_id: str, sport: Sport, year: int) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        USER_ROUTE,
        user_id,
        LEAGUES_ROUTE,
        sport.value.lower(),
        year,
    )
    return get(url)


def get_rosters(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        ROSTERS_ROUTE,
    )
    return get(url)


def get_users_in_league(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        USERS_ROUTE,
    )
    return get(url)


def get_matchups_for_week(*, league_id: str, week: int) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        MATCHUPS_ROUTE,
        week,
    )
    return get(url)
