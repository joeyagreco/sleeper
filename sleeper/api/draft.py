from sleeper.api._constants import (
    DRAFT_ROUTE,
    DRAFTS_ROUTE,
    LEAGUE_ROUTE,
    PICKS_ROUTE,
    SLEEPER_APP_BASE_URL,
    TRADED_PICKS_ROUTE,
    USER_ROUTE,
    VERSION,
)
from sleeper.api._types import Sport
from sleeper.api._utils import build_route, get


def get_user_drafts_for_year(*, user_id: str, sport: Sport, year: int) -> list[dict]:
    return get(
        build_route(
            SLEEPER_APP_BASE_URL,
            VERSION,
            USER_ROUTE,
            user_id,
            DRAFTS_ROUTE,
            sport,
            year,
        )
    )


def get_drafts_in_league(*, league_id: str) -> list[dict]:
    return get(
        build_route(
            SLEEPER_APP_BASE_URL,
            VERSION,
            LEAGUE_ROUTE,
            league_id,
            DRAFTS_ROUTE,
        )
    )


def get_draft(*, draft_id: str) -> dict:
    return get(build_route(SLEEPER_APP_BASE_URL, VERSION, DRAFT_ROUTE, draft_id))


def get_player_draft_picks(*, draft_id: str) -> list[dict]:
    return get(
        build_route(
            SLEEPER_APP_BASE_URL,
            VERSION,
            DRAFT_ROUTE,
            draft_id,
            PICKS_ROUTE,
        )
    )


def get_traded_draft_picks(*, draft_id: str) -> list[dict]:
    return get(
        build_route(
            SLEEPER_APP_BASE_URL,
            VERSION,
            DRAFT_ROUTE,
            draft_id,
            TRADED_PICKS_ROUTE,
        )
    )
