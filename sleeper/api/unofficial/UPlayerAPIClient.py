from typing import Any

from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum import PlayerPosition, SeasonType
from sleeper.enum.Sport import Sport
from sleeper.model.PlayerStats import PlayerStats


class UPlayerAPIClient(SleeperAPIClient):
    @classmethod
    def get_player_stats(
        cls, *, sport: Sport, player_id: str, season: str, **kwargs
    ) -> PlayerStats:
        """
        Gets player stats for the given season OR just the given week.
        """
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        week: int = kwargs.pop("week", None)

        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            None,
            cls._STATS_ROUTE,
            sport.name.lower(),
            cls._PLAYER_ROUTE,
            player_id,
        )
        url = cls._add_filters(
            url, ("season_type", season_type.name.lower()), ("season", season), ("week", week)
        )

        response_dict = cls._get(url)
        if response_dict is None:
            error_message = f"Could not get PlayerStats for sport: '{sport.name}', player_id: '{player_id}', season_type: '{season_type}', season: '{season}'"
            if week is not None:
                error_message += f", week: '{week}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict(response_dict)

    @classmethod
    def get_player_projections(
        cls, *, sport: Sport, player_id: str, season: str, **kwargs
    ) -> PlayerStats:
        """
        Gets player projections for the given season OR just the given week.
        """
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        week: int = kwargs.pop("week", None)

        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            None,
            cls._PROJECTIONS_ROUTE,
            sport.name.lower(),
            cls._PLAYER_ROUTE,
            player_id,
        )
        url = cls._add_filters(
            url, ("season_type", season_type.name.lower()), ("season", season), ("week", week)
        )

        response_dict = cls._get(url)
        if response_dict is None:
            error_message = f"Could not get PlayerStats for sport: '{sport.name}', player_id: '{player_id}', season_type: '{season_type}', season: '{season}'"
            if week is not None:
                error_message += f", week: '{week}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict(response_dict)

    @classmethod
    def get_all_player_stats(
        cls, *, sport: Sport, season: str, week: int, **kwargs
    ) -> list[PlayerStats]:
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        positions: list[PlayerPosition] = kwargs.pop("positions", list())

        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL, None, cls._STATS_ROUTE, sport.name.lower(), season, week
        )
        filters: list[tuple[str, Any]] = [("season_type", season_type.name.lower())]
        for position in positions:
            filters.append(("position[]", position.name.upper()))
        url = cls._add_filters(url, *filters)

        response_list = cls._get(url)
        if response_list is None:
            error_message = f"Could not get PlayerStats list for sport: '{sport.name}', season_type: '{season_type}', season: '{season}', week: '{week}'"
            if week is not None:
                error_message += f", week: '{week}'"
            if len(positions) > 0:
                error_message += f", positions: '{positions}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict_list(response_list)

    @classmethod
    def get_all_player_projections(
        cls, *, sport: Sport, season: str, week: int, **kwargs
    ) -> list[PlayerStats]:
        season_type: SeasonType = kwargs.pop("season_type", SeasonType.REGULAR)
        positions: list[PlayerPosition] = kwargs.pop("positions", list())

        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            None,
            cls._PROJECTIONS_ROUTE,
            sport.name.lower(),
            season,
            week,
        )
        filters: list[tuple[str, Any]] = [("season_type", season_type.name.lower())]
        for position in positions:
            filters.append(("position[]", position.name.upper()))
        url = cls._add_filters(url, *filters)

        response_list = cls._get(url)
        if response_list is None:
            error_message = f"Could not get PlayerStats list for sport: '{sport.name}', season_type: '{season_type}', season: '{season}', week: '{week}'"
            if week is not None:
                error_message += f", week: '{week}'"
            if len(positions) > 0:
                error_message += f", positions: '{positions}'"
            error_message += "."
            raise ValueError(error_message)
        return PlayerStats.from_dict_list(response_list)

    @classmethod
    def get_player_head_shot(cls, *, sport: Sport, player_id: str, save_to_path: str) -> None:
        """
        save_to_path should end in ".png".
        """

        url = cls._build_route(
            cls._SLEEPER_CDN_BASE_URL,
            None,
            cls._CONTENT_ROUTE,
            sport.name.lower(),
            cls._PLAYERS_ROUTE,
            player_id,
        )
        url += ".jpg"
        image_file = cls._get_image_file(url)
        image_file.save(save_to_path)
