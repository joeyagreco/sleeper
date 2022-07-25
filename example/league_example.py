from sleeper.api import LeagueAPIClient
from sleeper.enum import Sport
from sleeper.model import League, Roster, User, Matchup, PlayoffMatchup, Transaction, TradedPick, SportState

if __name__ == "__main__":
    # get a league by its ID
    league: League = LeagueAPIClient.get_league(league_id="my_league_id")

    # get all leagues for a user by its ID in a particular year
    user_leagues: list[League] = LeagueAPIClient.get_user_leagues_for_year(user_id="my_user_id", sport=Sport.NFL,
                                                                           year="2020")

    # get all rosters in a particular league
    league_rosters: list[Roster] = LeagueAPIClient.get_rosters(league_id="my_league_id")

    # get all users in a particular league
    league_users: list[User] = LeagueAPIClient.get_users_in_league(league_id="my_league_id")

    # get all matchups in a week for a particular league
    week_1_matchups: list[Matchup] = LeagueAPIClient.get_matchups_for_week(league_id="my_league_id", week=1)

    # get the winners bracket for a particular league
    winners_bracket: list[PlayoffMatchup] = LeagueAPIClient.get_winners_bracket(league_id="my_league_id")

    # get the losers bracket for a particular league
    losers_bracket: list[PlayoffMatchup] = LeagueAPIClient.get_losers_bracket(league_id="my_league_id")

    # get all transactions in a week for a particular league
    week_1_transactions: list[Transaction] = LeagueAPIClient.get_transactions(league_id="my_league_id", week=1)

    # get all traded picks for a particular league
    traded_picks: list[TradedPick] = LeagueAPIClient.get_traded_picks(league_id="my_league_id")

    # get the state of a particular sport
    nfl_state: SportState = LeagueAPIClient.get_sport_state(sport=Sport.NFL)
