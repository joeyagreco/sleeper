from typing import Optional

from sleeper.api._constants import (
    PLAYERS_ROUTE,
    SLEEPER_APP_BASE_URL,
    TRENDING_ROUTE,
    VERSION,
)
from sleeper.api._types import Sport, TrendType
from sleeper.api._utils import add_filters, build_route, get


def get_all_players(*, sport: Sport) -> dict[str, dict]:
    return get(
        build_route(
            SLEEPER_APP_BASE_URL,
            VERSION,
            PLAYERS_ROUTE,
            sport,
        )
    )


def get_trending_players(
    *,
    sport: Sport,
    trend_type: TrendType,
    lookback_hours: Optional[int] = None,
    limit: Optional[int] = None,
) -> list[dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        PLAYERS_ROUTE,
        sport,
        TRENDING_ROUTE,
        trend_type,
    )
    if lookback_hours is not None:
        url = add_filters(url, ("lookback_hours", lookback_hours))
    if limit is not None:
        url = add_filters(url, ("limit", limit))
    return get(url)
