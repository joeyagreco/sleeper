from abc import ABC

import requests

from sleeper.util.ConfigReader import ConfigReader


class APIClient(ABC):
    """
    Should be inherited by all API Clients.

    Sleeper API Documentation: https://docs.sleeper.app/
    """
    __BASE_URL = ConfigReader.get("api", "base_url")
    __VERSION = ConfigReader.get("api", "version")

    # ROUTES
    _DRAFT_ROUTE = ConfigReader.get("api", "draft_route")
    _DRAFTS_ROUTE = ConfigReader.get("api", "drafts_route")
    _LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
    _LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
    _LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
    _MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
    _PICKS_ROUTE = ConfigReader.get("api", "picks_route")
    _PLAYERS_ROUTE = ConfigReader.get("api", "players_route")
    _ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
    _STATE_ROUTE = ConfigReader.get("api", "state_route")
    _TRADED_PICKS_ROUTE = ConfigReader.get("api", "traded_picks_route")
    _TRANSACTIONS_ROUTE = ConfigReader.get("api", "transactions_route")
    _TRENDING_ROUTE = ConfigReader.get("api", "trending_route")
    _USER_ROUTE = ConfigReader.get("api", "user_route")
    _USERS_ROUTE = ConfigReader.get("api", "users_route")
    _WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")

    @classmethod
    def _build_route(cls, *args) -> str:
        args = (str(arg).replace("/", "") for arg in args)
        routes = "/".join(args)
        return f"{cls.__BASE_URL}/{cls.__VERSION}/{routes}"

    @staticmethod
    def _get(url: str) -> dict:
        # TODO: error handling
        response = requests.get(url)
        return requests.get(url).json()
