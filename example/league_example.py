from sleeper.api import (
    get_league,
    get_losers_bracket,
    get_matchups_for_week,
    get_rosters,
    get_sport_state,
    get_traded_picks,
    get_transactions,
    get_user_leagues_for_year,
    get_users_in_league,
    get_winners_bracket,
)

if __name__ == "__main__":
    # get a league by its ID
    league = get_league(league_id="my_league_id")

    # get all leagues for a user by its ID in a year
    user_leagues = get_user_leagues_for_year(
        user_id="my_user_id", sport="nfl", year=2023
    )

    # get all rosters in a league
    league_rosters = get_rosters(league_id="my_league_id")

    # get all users in a league
    league_users = get_users_in_league(league_id="my_league_id")

    # get all matchups in a week for a league
    week_1_matchups = get_matchups_for_week(league_id="my_league_id", week=1)

    # get the winners bracket for a league
    winners_bracket = get_winners_bracket(league_id="my_league_id")

    # get the losers bracket for a league
    losers_bracket = get_losers_bracket(league_id="my_league_id")

    # get all transactions in a week for a league
    week_1_transactions = get_transactions(league_id="my_league_id", week=1)

    # get all traded picks for a league
    traded_picks = get_traded_picks(league_id="my_league_id")

    # get the state of a sport
    nfl_state = get_sport_state(sport="nfl")
