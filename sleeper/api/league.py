from sleeper.api.constants import (
    LEAGUE_ROUTE,
    LEAGUES_ROUTE,
    LOSERS_BRACKET_ROUTE,
    MATCHUPS_ROUTE,
    ROSTERS_ROUTE,
    SLEEPER_APP_BASE_URL,
    TRADED_PICKS_ROUTE,
    TRANSACTIONS_ROUTE,
    USER_ROUTE,
    USERS_ROUTE,
    VERSION,
    WINNERS_BRACKET_ROUTE,
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


def get_winners_bracket(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        WINNERS_BRACKET_ROUTE,
    )
    return get(url)


def get_losers_bracket(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        LOSERS_BRACKET_ROUTE,
    )
    return get(url)


def get_transactions(*, league_id: str, week: int) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        TRANSACTIONS_ROUTE,
        week,
    )
    return get(url)


def get_traded_picks(*, league_id: str) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        LEAGUE_ROUTE,
        league_id,
        TRADED_PICKS_ROUTE,
    )
    return get(url)
