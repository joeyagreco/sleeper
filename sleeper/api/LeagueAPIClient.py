from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.Status import Status
from sleeper.model.League import League
from sleeper.model.Settings import Settings
from sleeper.util.ConfigReader import ConfigReader


class LeagueAPIClient(APIClient):

    def __init__(self, *, user_id: str, year: str):
        self.__user_id = user_id
        self.__year = year

        self.__LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
        self.__USER_ROUTE = ConfigReader.get("api", "user_route")
        self.__SPORT = Sport.NFL  # For now, only NFL is supported in the API, when other sports are added, this can be passed in

    @staticmethod
    def __build_settings_object(settings_dict: dict) -> Settings:
        return Settings(waiver_type=settings_dict["waiver_type"],
                        waiver_day_of_week=settings_dict["waiver_day_of_week"],
                        waiver_clear_days=settings_dict["waiver_clear_days"],
                        waiver_budget=settings_dict["waiver_budget"],
                        type=settings_dict["type"],
                        trade_review_days=settings_dict["trade_review_days"],
                        trade_deadline=settings_dict["trade_deadline"],
                        start_week=settings_dict["start_week"],
                        reserve_slots=settings_dict["reserve_slots"],
                        reserve_allow_out=settings_dict["reserve_allow_out"],
                        playoff_week_start=settings_dict["playoff_week_start"],
                        playoff_teams=settings_dict["playoff_teams"],
                        pick_trading=settings_dict["pick_trading"],
                        offseason_adds=settings_dict["offseason_adds"],
                        num_teams=settings_dict["num_teams"],
                        max_keepers=settings_dict["max_keepers"],
                        leg=settings_dict["leg"],
                        last_scored_leg=settings_dict["last_scored_leg"],
                        last_report=settings_dict["last_report"],
                        draft_rounds=settings_dict["draft_rounds"])

    @classmethod
    def __build_league_object(cls, league_dict: dict) -> League:
        return League(total_rosters=league_dict["total_rosters"],
                      status=Status.from_str(league_dict["status"]),
                      sport=Sport.from_str(league_dict["sport"]),
                      settings=cls.__build_settings_object(league_dict["settings"]),
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
