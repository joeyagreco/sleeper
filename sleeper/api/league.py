from sleeper.api.constants import (
    LEAGUE_ROUTE,
    SLEEPER_APP_BASE_URL,
    VERSION,
)
from sleeper.api.util import build_route, get


def get_league(*, league_id: str) -> dict:
    url = build_route(SLEEPER_APP_BASE_URL, VERSION, LEAGUE_ROUTE, league_id)
    return get(url)
