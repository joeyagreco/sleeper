from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.model.League import League
from sleeper.model.Matchup import Matchup
from sleeper.model.PlayoffMatchup import PlayoffMatchup
from sleeper.model.Roster import Roster
from sleeper.model.TradedPick import TradedPick
from sleeper.model.Transaction import Transaction
from sleeper.model.User import User
from sleeper.util.ConfigReader import ConfigReader


class LeagueAPIClient(APIClient):
    __LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
    __LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
    __USER_ROUTE = ConfigReader.get("api", "user_route")
    __USERS_ROUTE = ConfigReader.get("api", "users_route")
    __ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
    __MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
    __WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")
    __LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
    __TRANSACTIONS_ROUTE = ConfigReader.get("api", "transactions_route")
    __TRADED_PICKS_ROUTE = ConfigReader.get("api", "traded_picks_route")
    __SPORT = Sport.NFL  # For now, only NFL is supported in the API, when other sports are added, this can be passed in

    @classmethod
    def get_league(cls, *, league_id: str) -> League:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id)
        return League.from_dict(cls._get(url))

    @classmethod
    def get_user_leagues_for_year(cls, *, user_id: str, year: str) -> list[League]:
        url = cls._build_route(cls.__USER_ROUTE, user_id, cls.__LEAGUES_ROUTE, cls.__SPORT.value.lower(), year)
        return League.from_dict_list(cls._get(url))

    @classmethod
    def get_rosters(cls, *, league_id: str) -> list[Roster]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__ROSTERS_ROUTE)
        return Roster.from_dict_list(cls._get(url))

    @classmethod
    def get_users_in_league(cls, *, league_id: str) -> list[User]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__USERS_ROUTE)
        return User.from_dict_list(cls._get(url))

    @classmethod
    def get_matchups_for_week(cls, *, league_id: str, week: int) -> list[Matchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__MATCHUPS_ROUTE, week)
        return Matchup.from_dict_list(cls._get(url))

    @classmethod
    def get_winners_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__WINNERS_BRACKET_ROUTE)
        return PlayoffMatchup.from_dict_str(cls._get(url))

    @classmethod
    def get_losers_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__LOSERS_BRACKET_ROUTE)
        return PlayoffMatchup.from_dict_str(cls._get(url))

    @classmethod
    def get_transactions(cls, *, league_id: str, week: int) -> list[Transaction]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__TRANSACTIONS_ROUTE, week)
        return Transaction.from_dict_list(cls._get(url))

    @classmethod
    def get_traded_picks(cls, *, league_id: str) -> list[TradedPick]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__TRADED_PICKS_ROUTE)
        return TradedPick.from_dict_list(cls._get(url))
