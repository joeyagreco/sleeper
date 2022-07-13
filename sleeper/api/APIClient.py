from abc import ABC

from sleeper.util.ConfigReader import ConfigReader


class APIClient(ABC):
    """
    Should be inherited by all API Clients.
    """
    __BASE_URL = ConfigReader.get("api", "base_url")
    __VERSION = ConfigReader.get("api", "version")

    def _build_route(self, *args) -> str:
        routes = "/".join(args)
        return f"{self.__BASE_URL}/{self.__VERSION}{routes}"
