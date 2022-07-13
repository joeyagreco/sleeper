from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.Status import Status
from sleeper.model.League import League
from sleeper.util.ConfigReader import ConfigReader


class LeagueAPIClient(APIClient):

    def __init__(self, *, user_id: str, year: str):
        self.__user_id = user_id
        self.__year = year

        self.__LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
        self.__USER_ROUTE = ConfigReader.get("api", "user_route")
        self.__SPORT = Sport.NFL  # For now, only NFL is supported in the API, when other sports are added, this can be passed in

    @staticmethod
    def __build_league_object(league_dict: dict) -> League:
        return League(total_rosters=league_dict["total_rosters"],
                      status=Status.from_str(league_dict["status"]),
                      sport=Sport.from_str(league_dict["sport"]),
                      settings=None,
                      season_type=None,
                      season=league_dict["season"],
                      scoring_settings=None,
                      roster_positions=list(),
                      previous_league_id=league_dict["previous_league_id"],
                      name=league_dict["name"],
                      league_id=league_dict["league_id"],
                      draft_id=league_dict["draft_id"],
                      avatar=league_dict["avatar"])

    def get_league(self) -> League:
        url = self._build_route(self.__USER_ROUTE, self.__user_id, self.__LEAGUES_ROUTE, self.__SPORT.value.lower(),
                                self.__year)
        return self.__build_league_object(self._get(url)[0])
