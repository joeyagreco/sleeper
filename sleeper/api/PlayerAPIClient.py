from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.model.Player import Player


class PlayerAPIClient(APIClient):

    @classmethod
    def get_all_players(cls, *, sport: Sport) -> dict[str, Player]:
        url = cls._build_route(cls._PLAYERS_ROUTE, sport.name.lower())
        return Player.dict_by_id(cls._get(url))
