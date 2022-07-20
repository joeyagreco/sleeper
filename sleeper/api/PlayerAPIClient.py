from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.TrendType import TrendType
from sleeper.model.Player import Player
from sleeper.model.PlayerTrend import PlayerTrend


class PlayerAPIClient(APIClient):

    @classmethod
    def get_all_players(cls, *, sport: Sport) -> dict[str, Player]:
        url = cls._build_route(cls._PLAYERS_ROUTE, sport.name.lower())
        return Player.dict_by_id(cls._get(url))

    @classmethod
    def get_trending_players(cls, *, sport: Sport, trend_type: TrendType) -> list[PlayerTrend]:
        url = cls._build_route(cls._PLAYERS_ROUTE, sport.name.lower(), cls._TRENDING_ROUTE, trend_type.name.lower())
        return PlayerTrend.from_dict_list(cls._get(url))
