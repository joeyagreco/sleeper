from typing import Optional

from sleeper.api.APIClient import APIClient
from sleeper.enum.Sport import Sport
from sleeper.enum.TransactionStatus import TransactionStatus
from sleeper.enum.TransactionType import TransactionType
from sleeper.model.DraftPick import DraftPick
from sleeper.model.FAABTransaction import FAABTransaction
from sleeper.model.FromPlayoffMatchup import FromPlayoffMatchup
from sleeper.model.League import League
from sleeper.model.Matchup import Matchup
from sleeper.model.PlayoffMatchup import PlayoffMatchup
from sleeper.model.Roster import Roster
from sleeper.model.TradedPick import TradedPick
from sleeper.model.Transaction import Transaction
from sleeper.model.TransactionSettings import TransactionSettings
from sleeper.util.ConfigReader import ConfigReader


class LeagueAPIClient(APIClient):
    __LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
    __LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
    __USER_ROUTE = ConfigReader.get("api", "user_route")
    __ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
    __MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
    __WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")
    __LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
    __TRANSACTIONS_ROUTE = ConfigReader.get("api", "transactions_route")
    __TRADED_PICKS_ROUTE = ConfigReader.get("api", "traded_picks_route")
    __SPORT = Sport.NFL  # For now, only NFL is supported in the API, when other sports are added, this can be passed in

    @classmethod
    def __build_leagues_list(cls, league_dict_list: dict) -> list[League]:
        leagues = list()
        for league_dict in league_dict_list:
            leagues.append(League.from_dict(league_dict))
        return leagues

    # @classmethod
    # def __build_roster_object(cls, roster_dict: dict) -> Roster:
    #     return Roster(starters=roster_dict["starters"],
    #                   settings=RosterSettings.from_dict(roster_dict["settings"]),
    #                   roster_id=roster_dict["roster_id"],
    #                   reserve=roster_dict["reserve"],
    #                   players=roster_dict["players"],
    #                   owner_id=roster_dict["owner_id"],
    #                   league_id=roster_dict["league_id"])

    @classmethod
    def __build_rosters_list(cls, roster_dict_list: dict) -> list[Roster]:
        rosters = list()
        for roster_dict in roster_dict_list:
            rosters.append(Roster.from_dict(roster_dict))
        return rosters

    @classmethod
    def __build_matchup_object(cls, matchup_object_dict: dict) -> Matchup:
        return Matchup(starters=matchup_object_dict["starters"],
                       roster_id=matchup_object_dict["roster_id"],
                       players=matchup_object_dict["players"],
                       matchup_id=matchup_object_dict["matchup_id"],
                       points=matchup_object_dict["points"],
                       custom_points=matchup_object_dict["custom_points"])

    @classmethod
    def __build_matchups_list(cls, matchup_dict_list: dict) -> list[Matchup]:
        matchups = list()
        for matchup_dict in matchup_dict_list:
            matchups.append(cls.__build_matchup_object(matchup_dict))
        return matchups

    @classmethod
    def __build_from_playoff_matchup_object(cls, from_playoff_matchup_object: Optional[dict]) -> Optional[
        FromPlayoffMatchup]:
        if from_playoff_matchup_object is None:
            return None
        return FromPlayoffMatchup(won_matchup_id=from_playoff_matchup_object.get("w", None),
                                  lost_matchup_id=from_playoff_matchup_object.get("l", None))

    @classmethod
    def __build_playoff_matchup_object(cls, playoff_matchup_object: dict) -> PlayoffMatchup:
        return PlayoffMatchup(round=playoff_matchup_object["r"],
                              matchup_id=playoff_matchup_object["m"],
                              team_1_roster_id=playoff_matchup_object["t1"],
                              team_2_roster_id=playoff_matchup_object["t2"],
                              winning_roster_id=playoff_matchup_object["w"],
                              losing_roster_id=playoff_matchup_object["l"],
                              team_1_from=cls.__build_from_playoff_matchup_object(
                                  playoff_matchup_object.get("t1_from", None)),
                              team_2_from=cls.__build_from_playoff_matchup_object(
                                  playoff_matchup_object.get("t2_from", None)))

    @classmethod
    def __build_playoff_matchups_list(cls, playoff_matchup_dict_list: dict) -> list[PlayoffMatchup]:
        playoff_matchups = list()
        for playoff_matchup_dict in playoff_matchup_dict_list:
            playoff_matchups.append(cls.__build_playoff_matchup_object(playoff_matchup_dict))
        return playoff_matchups

    @classmethod
    def __build_transaction_settings_object(cls, transaction_settings_dict: Optional[dict]) -> Optional[
        TransactionSettings]:
        if transaction_settings_dict is None:
            return None
        return TransactionSettings(waiver_bid=transaction_settings_dict.get("waiver_bid", None),
                                   seq=transaction_settings_dict.get("seq", None))

    @classmethod
    def __build_draft_pick_object(cls, draft_pick_dict: dict) -> DraftPick:
        return DraftPick(season=draft_pick_dict["season"],
                         round=draft_pick_dict["round"],
                         roster_id=draft_pick_dict["roster_id"],
                         previous_owner_id=draft_pick_dict["previous_owner_id"],
                         owner_id=draft_pick_dict["owner_id"])

    @classmethod
    def __build_draft_pick_list(cls, draft_pick_dict_list: dict) -> list[DraftPick]:
        draft_picks = list()
        for draft_pick_dict in draft_pick_dict_list:
            draft_picks.append(cls.__build_draft_pick_object(draft_pick_dict))
        return draft_picks

    @classmethod
    def __build_faab_transaction(cls, faab_transaction_dict: dict) -> FAABTransaction:
        return FAABTransaction(sender=faab_transaction_dict["sender"],
                               receiver=faab_transaction_dict["receiver"],
                               amount=faab_transaction_dict["amount"])

    @classmethod
    def __build_faab_transaction_list(cls, faab_transaction_dict_list: dict) -> list[FAABTransaction]:
        faab_transactions = list()
        for faab_transaction_dict in faab_transaction_dict_list:
            faab_transactions.append(cls.__build_faab_transaction(faab_transaction_dict))
        return faab_transactions

    @classmethod
    def __build_transaction_object(cls, transaction_dict: dict) -> Transaction:
        return Transaction(type=TransactionType.from_str(transaction_dict["type"]),
                           transaction_id=transaction_dict["transaction_id"],
                           status_updated=transaction_dict["status_updated"],
                           status=TransactionStatus.from_str(transaction_dict["status"]),
                           settings=cls.__build_transaction_settings_object(transaction_dict["settings"]),
                           roster_ids=transaction_dict["roster_ids"],
                           week=transaction_dict["leg"],
                           adds=transaction_dict["adds"],
                           drops=transaction_dict["drops"],
                           draft_picks=cls.__build_draft_pick_list(transaction_dict["draft_picks"]),
                           creator=transaction_dict["creator"],
                           created=transaction_dict["created"],
                           consenter_ids=transaction_dict["consenter_ids"],
                           waiver_budget=cls.__build_faab_transaction_list(transaction_dict["waiver_budget"]))

    @classmethod
    def __build_transaction_list(cls, transaction_dict_list: dict) -> list[Transaction]:
        transactions = list()
        for transaction_dict in transaction_dict_list:
            transactions.append(cls.__build_transaction_object(transaction_dict))
        return transactions

    @classmethod
    def __build_traded_pick_object(cls, traded_pick_dict: dict) -> TradedPick:
        return TradedPick(season=traded_pick_dict.get("season", None),
                          round=traded_pick_dict.get("round", None),
                          roster_id=traded_pick_dict.get("roster_id", None),
                          previous_owner_id=traded_pick_dict.get("previous_owner_id", None),
                          owner_id=traded_pick_dict.get("owner_id", None))

    @classmethod
    def __build_traded_pick_list(cls, traded_pick_dict_list: dict) -> list[TradedPick]:
        traded_picks = list()
        for traded_pick_dict in traded_pick_dict_list:
            traded_picks.append(cls.__build_traded_pick_object(traded_pick_dict))
        return traded_picks

    @classmethod
    def get_league(cls, *, league_id: str) -> League:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id)
        return League.from_dict(cls._get(url))

    @classmethod
    def get_user_leagues_for_year(cls, *, user_id: str, year: str) -> list[League]:
        url = cls._build_route(cls.__USER_ROUTE, user_id, cls.__LEAGUES_ROUTE, cls.__SPORT.value.lower(), year)
        return cls.__build_leagues_list(cls._get(url))

    @classmethod
    def get_rosters(cls, *, league_id: str) -> list[Roster]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__ROSTERS_ROUTE)
        return cls.__build_rosters_list(cls._get(url))

    @classmethod
    def get_matchups_for_week(cls, *, league_id: str, week: int) -> list[Matchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__MATCHUPS_ROUTE, week)
        return cls.__build_matchups_list(cls._get(url))

    @classmethod
    def get_winners_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__WINNERS_BRACKET_ROUTE)
        return cls.__build_playoff_matchups_list(cls._get(url))

    @classmethod
    def get_losers_bracket(cls, *, league_id: str) -> list[PlayoffMatchup]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__LOSERS_BRACKET_ROUTE)
        return cls.__build_playoff_matchups_list(cls._get(url))

    @classmethod
    def get_transactions(cls, *, league_id: str, week: int) -> list[Transaction]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__TRANSACTIONS_ROUTE, week)
        return cls.__build_transaction_list(cls._get(url))

    @classmethod
    def get_traded_picks(cls, *, league_id: str) -> list[TradedPick]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__TRADED_PICKS_ROUTE)
        return cls.__build_traded_pick_list(cls._get(url))
