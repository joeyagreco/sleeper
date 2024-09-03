from sleeper.api.constants import PLAYERS_ROUTE, SLEEPER_APP_BASE_URL, VERSION
from sleeper.api.util import build_route, get
from sleeper.enum.Sport import Sport

_DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS = 24
_DEFAULT_TRENDING_PLAYERS_LIMIT = 25


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


# @classmethod
# def get_trending_players(
#     cls,
#     *,
#     sport: Sport,
#     trend_type: TrendType,
#     lookback_hours: int = None,
#     limit: int = None,
# ) -> list[PlayerTrend]:
#     if lookback_hours is None:
#         lookback_hours = cls.__DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS
#     if limit is None:
#         limit = cls.__DEFAULT_TRENDING_PLAYERS_LIMIT
#     url = cls._build_route(
#         cls._SLEEPER_APP_BASE_URL,
#         cls._VERSION,
#         cls._PLAYERS_ROUTE,
#         sport.name.lower(),
#         cls._TRENDING_ROUTE,
#         trend_type.name.lower(),
#     )
#     url = cls._add_filters(url, ("lookback_hours", lookback_hours), ("limit", limit))
#     response_dict = cls._get(url)
#     if response_dict is None:
#         raise ValueError(f"Could not get PlayerTrends.")
#     return PlayerTrend.from_dict_list(response_dict)
