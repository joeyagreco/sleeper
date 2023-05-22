from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType
from sleeper.model.Player import Player
from sleeper.model.PlayerTrend import PlayerTrend


class PlayerAPIClient(SleeperAPIClient):
    __DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS = 24
    __DEFAULT_TRENDING_PLAYERS_LIMIT = 25

    @classmethod
    def get_all_players(cls, *, sport: Sport) -> dict[str, Player]:
        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL, cls._VERSION, cls._PLAYERS_ROUTE, sport.name.lower()
        )
        response_dict = cls._get(url)
        if response_dict is None:
            raise ValueError(f"Could not get Players for sport: '{sport.name}'.")
        return Player.dict_by_id(response_dict, sport)

    @classmethod
    def get_trending_players(
        cls, *, sport: Sport, trend_type: TrendType, **kwargs
    ) -> list[PlayerTrend]:
        lookback_hours = kwargs.pop("lookback_hours", cls.__DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS)
        limit = kwargs.pop("limit", cls.__DEFAULT_TRENDING_PLAYERS_LIMIT)
        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            cls._VERSION,
            cls._PLAYERS_ROUTE,
            sport.name.lower(),
            cls._TRENDING_ROUTE,
            trend_type.name.lower(),
        )
        url = cls._add_filters(url, ("lookback_hours", lookback_hours), ("limit", limit))
        response_dict = cls._get(url)
        if response_dict is None:
            raise ValueError(f"Could not get PlayerTrends.")
        return PlayerTrend.from_dict_list(response_dict)
