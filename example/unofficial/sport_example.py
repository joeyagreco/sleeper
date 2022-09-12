from sleeper.api.unofficial import USportAPIClient
from sleeper.enum import Sport
from sleeper.model import Game

if __name__ == "__main__":
    # get regular season schedule for a particular sport and season
    regular_season: list[Game] = USportAPIClient.get_regular_season_schedule(sport=Sport.NFL, season="2020")
