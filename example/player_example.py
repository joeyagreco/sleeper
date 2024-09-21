from sleeper.api import get_all_players, get_trending_players

if __name__ == "__main__":
    # get all players in a sport
    nfl_players = get_all_players(sport="nfl")

    # get players that are trending up in a sport
    nfl_trending_up_players = get_trending_players(sport="nfl", trend_type="add")

    # get players that are trending down in a sport
    nfl_trending_down_players = get_trending_players(sport="nfl", trend_type="drop")
