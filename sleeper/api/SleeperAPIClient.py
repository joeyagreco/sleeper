import io
from abc import ABC
from typing import Optional

import requests
from PIL import Image

from sleeper.exception.SleeperAPIException import SleeperAPIException
from sleeper.util.ConfigReader import ConfigReader


class SleeperAPIClient(ABC):
    """
    Should be inherited by all API Clients.

    Sleeper API Documentation: https://docs.sleeper.app/
    """

    _SLEEPER_APP_BASE_URL = ConfigReader.get("api", "sleeper_app_base_url")
    _SLEEPER_CDN_BASE_URL = ConfigReader.get("api", "sleeper_cdn_base_url")
    _VERSION = ConfigReader.get("api", "version")

    # ROUTES
    _AVATARS_ROUTE = ConfigReader.get("api", "avatars_route")
    _CONTENT_ROUTE = ConfigReader.get("api", "content_route")
    _DEPTH_CHART_ROUTE = ConfigReader.get("api", "depth_chart_route")
    _DRAFT_ROUTE = ConfigReader.get("api", "draft_route")
    _DRAFTS_ROUTE = ConfigReader.get("api", "drafts_route")
    _LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
    _LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
    _LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
    _MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
    _PICKS_ROUTE = ConfigReader.get("api", "picks_route")
    _PLAYER_ROUTE = ConfigReader.get("api", "player_route")
    _PLAYERS_ROUTE = ConfigReader.get("api", "players_route")
    _PROJECTIONS_ROUTE = ConfigReader.get("api", "projections_route")
    _ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
    _SCHEDULE_ROUTE = ConfigReader.get("api", "schedule_route")
    _STATE_ROUTE = ConfigReader.get("api", "state_route")
    _STATS_ROUTE = ConfigReader.get("api", "stats_route")
    _THUMBS_ROUTE = ConfigReader.get("api", "thumbs_route")
    _TRADED_PICKS_ROUTE = ConfigReader.get("api", "traded_picks_route")
    _TRANSACTIONS_ROUTE = ConfigReader.get("api", "transactions_route")
    _TRENDING_ROUTE = ConfigReader.get("api", "trending_route")
    _USER_ROUTE = ConfigReader.get("api", "user_route")
    _USERS_ROUTE = ConfigReader.get("api", "users_route")
    _WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")

    @classmethod
    def _build_route(cls, base_url: str, version: Optional[str], *args) -> str:
        args = (str(arg).replace("/", "") for arg in args)
        if version is not None:
            return f"{base_url}/{version}/{'/'.join(args)}"
        else:
            return f"{base_url}/{'/'.join(args)}"

    @classmethod
    def _add_filters(cls, url: str, *args) -> str:
        """
        Adds filters to the given url.
        """
        if len(args) > 0:
            symbol = "?"
            for i, arg in enumerate(args):
                if i > 0:
                    symbol = "&"
                if arg[0] is not None and arg[1] is not None:
                    url = f"{url}{symbol}{arg[0]}={arg[1]}"
        return url

    @staticmethod
    def _get(url: str) -> Optional[dict | list]:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _get_image_file(url: str) -> Image:
        response = requests.get(url)
        response.raise_for_status()
        image_bytes = response.content
        if image_bytes is None:
            raise SleeperAPIException(f"No image found.")
        image_stream = io.BytesIO(image_bytes)
        return Image.open(image_stream)
