from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.PlayerStats import PlayerStats


class UPlayerAPIClient(SleeperAPIClient):

    @classmethod
    def get_player_stats(cls, *, sport: Sport, player_id: str, season: str, **kwargs) -> PlayerStats:
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        week: int = kwargs.pop("week", None)

        url = cls._build_route(cls._SLEEPER_APP_BASE_URL, None, cls._STATS_ROUTE, sport.name.lower(), cls._PLAYER_ROUTE,
                               player_id)
        url = cls._add_filters(url, ("season_type", season_type.name.lower()), ("season", season), ("week", week))

        response_dict = cls._get(url)
        if response_dict is None:
            error_message = f"Could not get PlayerStats for sport: '{sport.name}', player_id: '{player_id}', season_type: '{season_type}', season: '{season}'"
            if week is not None:
                error_message += f", week: '{week}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict(response_dict)

    @classmethod
    def get_player_projections(cls, *, sport: Sport, player_id: str, season: str, **kwargs) -> PlayerStats:
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        week: int = kwargs.pop("week", None)

        url = cls._build_route(cls._SLEEPER_APP_BASE_URL, None, cls._PROJECTIONS_ROUTE, sport.name.lower(),
                               cls._PLAYER_ROUTE, player_id)
        url = cls._add_filters(url, ("season_type", season_type.name.lower()), ("season", season), ("week", week))

        response_dict = cls._get(url)
        if response_dict is None:
            error_message = f"Could not get PlayerStats for sport: '{sport.name}', player_id: '{player_id}', season_type: '{season_type}', season: '{season}'"
            if week is not None:
                error_message += f", week: '{week}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict(response_dict)
