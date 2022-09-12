from sleeper.api.unofficial import UTeamAPIClient
from sleeper.enum import Sport
from sleeper.enum.nfl import NFLTeam
from sleeper.model import DepthChart

if __name__ == "__main__":
    # get depth chart for a particular sport and team
    depth_chart: DepthChart = UTeamAPIClient.get_team_depth_chart(sport=Sport.NFL, team=NFLTeam.GB)
