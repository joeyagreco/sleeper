from typing import Optional

from sleeper.api.constants import (
    DEFAULT_TRENDING_PLAYERS_LIMIT,
    DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS,
    PLAYERS_ROUTE,
    SLEEPER_APP_BASE_URL,
    TRENDING_ROUTE,
    VERSION,
)
from sleeper.api.util import add_filters, build_route, get
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType


def get_all_players(*, sport: Sport) -> dict[str, dict]:
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        PLAYERS_ROUTE,
        sport.name.lower(),
    )
    response_dict = get(url)
    if response_dict is None:
        raise ValueError(f"Could not get Players for sport: '{sport.name}'.")
    return response_dict


def get_trending_players(
    *,
    sport: Sport,
    trend_type: TrendType,
    lookback_hours: Optional[int] = None,
    limit: Optional[int] = None,
) -> list[dict]:
    if lookback_hours is None:
        lookback_hours = DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS
    if limit is None:
        limit = DEFAULT_TRENDING_PLAYERS_LIMIT
    url = build_route(
        SLEEPER_APP_BASE_URL,
        VERSION,
        PLAYERS_ROUTE,
        sport.name.lower(),
        TRENDING_ROUTE,
        trend_type.name.lower(),
    )
    url = add_filters(url, ("lookback_hours", lookback_hours), ("limit", limit))
    response_dict = get(url)
    if response_dict is None:
        raise ValueError(f"Could not get PlayerTrends.")
    return response_dict
