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

    @classmethod
    def _build_route(cls, *args) -> str:
        args = (str(arg).replace("/", "") for arg in args)
        routes = "/".join(args)
        return f"{cls.__BASE_URL}/{cls.__VERSION}/{routes}"

    @staticmethod
    def _get(url: str) -> dict:
        # TODO: error handling
        return requests.get(url).json()
