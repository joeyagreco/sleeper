from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType
from sleeper.model.Player import Player
from sleeper.model.PlayerTrend import PlayerTrend


class PlayerAPIClient(SleeperAPIClient):

    @classmethod
    def get_all_players(cls, *, sport: Sport) -> dict[str, Player]:
        url = cls._build_route(cls._SLEEPER_APP_BASE_URL, cls._VERSION, cls._PLAYERS_ROUTE, sport.name.lower())
        return Player.dict_by_id(cls._get(url))

    @classmethod
    def get_trending_players(cls, *, sport: Sport, trend_type: TrendType, **kwargs) -> list[PlayerTrend]:
        lookback_hours = kwargs.pop("lookback_hours", 24)
        limit = kwargs.pop("limit", 25)
        url = cls._build_route(cls._SLEEPER_APP_BASE_URL, cls._VERSION, cls._PLAYERS_ROUTE, sport.name.lower(),
                               cls._TRENDING_ROUTE, trend_type.name.lower())
        url = cls._add_filters(url, ("lookback_hours", lookback_hours), ("limit", limit))
        return PlayerTrend.from_dict_list(cls._get(url))
