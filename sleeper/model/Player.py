from __future__ import annotations

import datetime
from dataclasses import dataclass
from datetime import date
from typing import Any, Optional

from sleeper.enum.InjuryStatus import InjuryStatus
from sleeper.enum.PlayerPosition import PlayerPosition
from sleeper.enum.PlayerStatus import PlayerStatus
from sleeper.enum.PracticeParticipation import PracticeParticipation
from sleeper.enum.Sport import Sport
from sleeper.enum.SportTeam import SportTeam


@dataclass(kw_only=True)
class Player:
    active: bool
    age: int
    birth_city: str
    birth_country: str
    birth_date: date
    birth_state: str
    college: str
    depth_chart_order: int
    depth_chart_position: int
    espn_id: str
    fantasy_data_id: int
    fantasy_positions: list[PlayerPosition]
    first_name: str
    gsis_id: str
    hashtag: str
    height: str
    high_school: str
    injury_body_part: str
    injury_notes: str
    injury_start_date: str
    injury_status: InjuryStatus
    last_name: str
    metadata: dict[str, Any]
    news_updated: int
    number: int
    pandascore_id: str
    player_id: str
    position: PlayerPosition
    practice_description: str
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
    swish_id: int
    team: SportTeam
    weight: str
    yahoo_id: str
    years_exp: int

    @staticmethod
    def from_dict(player_dict: dict, sport: Sport) -> Optional[Player]:
        if player_dict is None:
            return None
        given_fantasy_positions = player_dict.get("fantasy_positions")
        fantasy_positions = (
            [PlayerPosition.enum(sport).from_str(pos) for pos in given_fantasy_positions]
            if given_fantasy_positions is not None
            else None
        )

        birth_date = (
            None
            if player_dict.get("birth_date") is None
            else datetime.datetime.strptime(player_dict.get("birth_date"), "%Y-%m-%d").date()
        )

        return Player(
            hashtag=player_dict.get("hashtag"),
            depth_chart_position=player_dict.get("depth_chart_position"),
            status=PlayerStatus.enum(sport).from_str(player_dict.get("status")),
            sport=sport,
            fantasy_positions=fantasy_positions,
            number=player_dict.get("number"),
            search_last_name=player_dict.get("search_last_name"),
            injury_start_date=player_dict.get("injury_start_date"),
            weight=player_dict.get("weight"),
            position=PlayerPosition.enum(sport).from_str(player_dict.get("position")),
            practice_participation=PracticeParticipation.from_str(
                player_dict.get("practice_participation")
            ),
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
            yahoo_id=player_dict.get("yahoo_id"),
            swish_id=player_dict.get("swish_id"),
            birth_city=player_dict.get("birth_city"),
            injury_notes=player_dict.get("injury_notes"),
            gsis_id=player_dict.get("gsis_id"),
            birth_state=player_dict.get("birth_state"),
            practice_description=player_dict.get("practice_description"),
            pandascore_id=player_dict.get("pandascore_id"),
            high_school=player_dict.get("high_school"),
            news_updated=player_dict.get("news_updated"),
            metadata=player_dict.get("metadata"),
            injury_body_part=player_dict.get("injury_body_part"),
            birth_date=birth_date,
            active=player_dict.get("active"),
        )

    @staticmethod
    def dict_by_id(player_dict_list: list, sport: Sport) -> dict[str, Player]:
        players_by_id = dict()
        for player_id in player_dict_list:
            players_by_id[player_id] = Player.from_dict(player_dict_list[player_id], sport)
        return players_by_id
