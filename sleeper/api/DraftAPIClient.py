from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.model.Draft import Draft
from sleeper.util.ConfigReader import ConfigReader


class DraftAPIClient(APIClient):
    __DRAFTS_ROUTE = ConfigReader.get("api", "drafts_route")
    __USER_ROUTE = ConfigReader.get("api", "user_route")

    @classmethod
    def get_user_drafts_for_year(cls, *, user_id: str, sport: Sport, year: str) -> list[Draft]:
        url = cls._build_route(cls.__USER_ROUTE, user_id, cls.__DRAFTS_ROUTE, sport.name.lower(), year)
        return Draft.from_dict_list(cls._get(url))
