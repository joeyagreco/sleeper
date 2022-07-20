from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.NFLPlayerStatus import PlayerStatus
from sleeper.enum.PlayerPosition import PlayerPosition
from sleeper.enum.PracticeParticipation import PracticeParticipation
from sleeper.enum.Sport import Sport
from sleeper.enum.SportTeam import SportTeam


@dataclass(kw_only=True)
class Player:
    hashtag: Optional[str]
    depth_chart_position: Optional[int]
    status: PlayerStatus
    sport: Sport
    fantasy_positions: list[PlayerPosition]
    number: Optional[int]
    search_last_name: Optional[str]
    injury_start_date: Optional[str]
    weight: Optional[str]
    position: PlayerPosition
    practice_participation: PracticeParticipation
    sportradar_id: Optional[str]
    team: SportTeam
    last_name: Optional[str]
    college: Optional[str]
    fantasy_data_id: Optional[int]
    injury_status: InjuryStatus
    player_id: Optional[str]
    height: Optional[str]
    search_full_name: Optional[str]
    age: Optional[int]
    stats_id: Optional[str]
    birth_country: Optional[str]
    espn_id: Optional[str]
    search_rank: Optional[int]
    first_name: Optional[str]
    depth_chart_order: int
    years_exp: int
    rotowire_id: Optional[int]
    rotoworld_id: Optional[int]
    search_first_name: Optional[str]
    yahoo_id: Optional[str]

    @staticmethod
    def from_dict(player_dict: dict) -> Player:
        given_fantasy_positions = player_dict.get("fantasy_positions", list())
        given_fantasy_positions = given_fantasy_positions if given_fantasy_positions is not None else list()
        fantasy_positions = [PlayerPosition.from_str(pos) for pos in given_fantasy_positions]

        return Player(hashtag=player_dict.get("hashtag", None),
                      depth_chart_position=player_dict.get("depth_chart_position", None),
                      status=PlayerStatus.from_str(player_dict.get("status", None)),
                      sport=Sport.from_str(player_dict.get("sport", None)),
                      fantasy_positions=fantasy_positions,
                      number=player_dict.get("number", None),
                      search_last_name=player_dict.get("search_last_name", None),
                      injury_start_date=player_dict.get("injury_start_date", None),
                      weight=player_dict.get("weight", None),
                      position=PlayerPosition.from_str(player_dict.get("position", None)),
                      practice_participation=PracticeParticipation.from_str(
                          player_dict.get("practice_participation", None)),
                      sportradar_id=player_dict.get("sportradar_id", None),
                      team=SportTeam.from_str(player_dict.get("team", None)),
                      last_name=player_dict.get("last_name", None),
                      college=player_dict.get("college", None),
                      fantasy_data_id=player_dict.get("fantasy_data_id", None),
                      injury_status=InjuryStatus.from_str(player_dict.get("injury_status", None)),
                      player_id=player_dict.get("player_id", None),
                      height=player_dict.get("height", None),
                      search_full_name=player_dict.get("player_full_name", None),
                      age=player_dict.get("age", None),
                      stats_id=player_dict.get("stats_id", None),
                      birth_country=player_dict.get("birth_country", None),
                      espn_id=player_dict.get("espn_id", None),
                      search_rank=player_dict.get("search_rank", None),
                      first_name=player_dict.get("first_name", None),
                      depth_chart_order=player_dict.get("depth_chart_order", None),
                      years_exp=player_dict.get("years_exp", None),
                      rotowire_id=player_dict.get("rotowire_id", None),
                      rotoworld_id=player_dict.get("rotoworld_id", None),
                      search_first_name=player_dict.get("search_first_name", None),
                      yahoo_id=player_dict.get("yahoo_id", None))

    @staticmethod
    def dict_by_id(player_dict_list: dict) -> dict[str, Player]:
        players_by_id = dict()
        for player_id in player_dict_list:
            players_by_id[player_id] = Player.from_dict(player_dict_list[player_id])
        return players_by_id
