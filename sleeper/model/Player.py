from __future__ import annotations

from dataclasses import dataclass

from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.PlayerPosition import PlayerPosition
from sleeper.enum.PlayerStatus import PlayerStatus
from sleeper.enum.PracticeParticipation import PracticeParticipation
from sleeper.enum.Sport import Sport
from sleeper.enum.SportTeam import SportTeam


@dataclass(kw_only=True)
class Player:
    age: int
    birth_country: str
    college: str
    depth_chart_order: int
    depth_chart_position: int
    espn_id: str
    fantasy_data_id: int
    fantasy_positions: list[PlayerPosition]
    first_name: str
    hashtag: str
    height: str
    injury_start_date: str
    injury_status: InjuryStatus
    last_name: str
    number: int
    player_id: str
    position: PlayerPosition
    practice_participation: PracticeParticipation
    rotowire_id: int
    rotoworld_id: int
    search_first_name: str
    search_full_name: str
    search_last_name: str
    search_rank: int
    sport: Sport
    sportradar_id: str
    stats_id: str
    status: PlayerStatus
    team: SportTeam
    weight: str
    yahoo_id: str
    years_exp: int

    @staticmethod
    def from_dict(player_dict: dict, sport: Sport) -> Player:
        given_fantasy_positions = player_dict.get("fantasy_positions")
        fantasy_positions = [PlayerPosition.enum(sport).from_str(pos) for pos in
                             given_fantasy_positions] if given_fantasy_positions is not None else None

        return Player(hashtag=player_dict.get("hashtag"),
                      depth_chart_position=player_dict.get("depth_chart_position"),
                      status=PlayerStatus.enum(sport).from_str(player_dict.get("status")),
                      sport=Sport.from_str(player_dict.get("sport")),
                      fantasy_positions=fantasy_positions,
                      number=player_dict.get("number"),
                      search_last_name=player_dict.get("search_last_name"),
                      injury_start_date=player_dict.get("injury_start_date"),
                      weight=player_dict.get("weight"),
                      position=PlayerPosition.enum(sport).from_str(player_dict.get("position")),
                      practice_participation=PracticeParticipation.from_str(
                          player_dict.get("practice_participation")),
                      sportradar_id=player_dict.get("sportradar_id"),
                      team=SportTeam.enum(sport).from_str(player_dict.get("team")),
                      last_name=player_dict.get("last_name"),
                      college=player_dict.get("college"),
                      fantasy_data_id=player_dict.get("fantasy_data_id"),
                      injury_status=InjuryStatus.from_str(player_dict.get("injury_status")),
                      player_id=player_dict.get("player_id"),
                      height=player_dict.get("height"),
                      search_full_name=player_dict.get("search_full_name"),
                      age=player_dict.get("age"),
                      stats_id=player_dict.get("stats_id"),
                      birth_country=player_dict.get("birth_country"),
                      espn_id=player_dict.get("espn_id"),
                      search_rank=player_dict.get("search_rank"),
                      first_name=player_dict.get("first_name"),
                      depth_chart_order=player_dict.get("depth_chart_order"),
                      years_exp=player_dict.get("years_exp"),
                      rotowire_id=player_dict.get("rotowire_id"),
                      rotoworld_id=player_dict.get("rotoworld_id"),
                      search_first_name=player_dict.get("search_first_name"),
                      yahoo_id=player_dict.get("yahoo_id"))

    @staticmethod
    def dict_by_id(player_dict_list: dict, sport: Sport) -> dict[str, Player]:
        players_by_id = dict()
        for player_id in player_dict_list:
            players_by_id[player_id] = Player.from_dict(player_dict_list[player_id], sport)
        return players_by_id
