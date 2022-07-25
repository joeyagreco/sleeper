from sleeper.api import PlayerAPIClient
from sleeper.enum import Sport, TrendType
from sleeper.model import Player, PlayerTrend

if __name__ == "__main__":
    # get all players in a particular sport
    nfl_players: dict[str, Player] = PlayerAPIClient.get_all_players(sport=Sport.NFL)

    # get all trending players that were added for a particular sport
    nfl_added_trending_players: list[PlayerTrend] = PlayerAPIClient.get_trending_players(sport=Sport.NFL,
                                                                                         trend_type=TrendType.ADD)

    # get all trending players that were dropped for a particular sport
    nfl_dropped_trending_players: list[PlayerTrend] = PlayerAPIClient.get_trending_players(sport=Sport.NFL,
                                                                                           trend_type=TrendType.DROP)
