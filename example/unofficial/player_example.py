from sleeper.api.unofficial import UPlayerAPIClient
from sleeper.enum import Sport
from sleeper.enum.nfl import NFLPosition
from sleeper.model import PlayerStats

if __name__ == "__main__":
    # get player stats for a player for a particular sport, week, and season
    player_stats_week: PlayerStats = UPlayerAPIClient.get_player_stats(
        sport=Sport.NFL, player_id="1234", season="2020", week=1
    )

    # get player stats for a player for the entire season in a particular sport and season
    player_stats_season: PlayerStats = UPlayerAPIClient.get_player_stats(
        sport=Sport.NFL, player_id="1234", season="2020"
    )

    # get player projections for a player for a particular sport, week, and season
    player_projections_week: PlayerStats = UPlayerAPIClient.get_player_projections(
        sport=Sport.NFL, player_id="1234", season="2020", week=1
    )

    # get player projections for a player for the entire season in a particular sport and season
    player_projections_season: PlayerStats = UPlayerAPIClient.get_player_projections(
        sport=Sport.NFL, player_id="1234", season="2020"
    )

    # get all player stats for a particular sport, season, and week
    all_player_stats: list[PlayerStats] = UPlayerAPIClient.get_all_player_stats(
        sport=Sport.NFL, season="2020", week=1
    )

    # get all player stats for QBs and RBs for a particular sport, season, and week
    all_player_stats_qbs_rbs: list[PlayerStats] = UPlayerAPIClient.get_all_player_stats(
        sport=Sport.NFL, season="2020", week=1, positions=[NFLPosition.QB, NFLPosition.RB]
    )

    # get all player projections for a particular sport, season, and week
    all_player_projections: list[PlayerStats] = UPlayerAPIClient.get_all_player_projections(
        sport=Sport.NFL, season="2020", week=1
    )

    # get all player projections for QBs and RBs for a particular sport, season, and week
    all_player_projections_qbs_rbs: list[PlayerStats] = UPlayerAPIClient.get_all_player_projections(
        sport=Sport.NFL, season="2020", week=1, positions=[NFLPosition.QB, NFLPosition.RB]
    )

    # get a player's headshot and save locally
    # the file path should save to a file that has the extension '.png'
    UPlayerAPIClient.get_player_head_shot(
        sport=Sport.NFL, player_id="1234", save_to_path="C:\\Desktop\\avatar\\my_headshot.png"
    )
