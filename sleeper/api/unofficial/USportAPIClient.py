from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum import SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.Game import Game


class USportAPIClient(SleeperAPIClient):
    @classmethod
    def get_regular_season_schedule(cls, *, sport: Sport, season: str, **kwargs) -> list[Game]:
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            None,
            cls._SCHEDULE_ROUTE,
            sport.name.lower(),
            season_type.name.lower(),
            season,
        )

        response_list = cls._get(url)
        if response_list is None:
            raise ValueError(
                f"Could not get Game list for sport: '{sport.name}', season: '{season}', season_type: '{season_type.name}'."
            )
        return Game.from_dict_list(response_list, sport)
