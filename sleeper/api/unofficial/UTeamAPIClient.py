from sleeper.api.SleeperAPIClient import SleeperAPIClient
from sleeper.enum import SportTeam
from sleeper.enum.Sport import Sport
from sleeper.model.DepthChart import DepthChart


class UTeamAPIClient(SleeperAPIClient):
    @classmethod
    def get_team_depth_chart(cls, *, sport: Sport, team: SportTeam) -> DepthChart:
        url = cls._build_route(
            cls._SLEEPER_APP_BASE_URL,
            None,
            cls._PLAYERS_ROUTE,
            sport.name.lower(),
            team.name.lower(),
            cls._DEPTH_CHART_ROUTE,
        )

        response_dict = cls._get(url)
        if response_dict is None:
            raise ValueError(
                f"Could not get DepthChart for sport: '{sport.name}', team: '{team.name}'"
            )
        return DepthChart.model(sport).from_dict(response_dict)
