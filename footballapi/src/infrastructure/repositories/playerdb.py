"""Module containing player repository abstractions."""

from typing import Any, Iterable

from sqlalchemy import select, func, case, or_

from src.core.repositories.iplayer import IPlayerRepository
from src.db import player_table, database, goal_table, card_table, match_table
from src.infrastructure.dto.playerdto import PlayerDTO


class PlayerRepository(IPlayerRepository):
    """A class representing implementation of player repository."""

    async def get_all_players(self) -> Iterable[Any]:
        """The abstract getting all players from the data storage.

        Returns:
            Iterable[Any]: Players in the data storage.
        """
        query = player_table.select()
        result = await database.fetch_all(query)
        return [PlayerDTO.from_record(player) for player in result]

    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting a player by provided player_api_id.

        Args:
            player_api_id (int): The api_id of the player.

        Returns:
            Any | None: The player details.
        """
        query = player_table.select().where(player_table.c.player_api_id == player_api_id)
        result = await database.fetch_one(query)
        return PlayerDTO.from_record(result)

    async def get_by_player_name(self, player_name: str) -> Any | None:
        """The abstract getting a player by their name.

        Args:
            player_name (str): The name of the player.

        Returns:
            Any | None: The player details.
        """
        query = player_table.select().where(player_table.c.player_name == player_name)
        result = await database.fetch_all(query)
        return [PlayerDTO.from_record(player) for player in result]

    async def get_stats(self, player_api_id: int) -> Any | None:
        """The abstract getting a player statistics by provided player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The requested stats.
        """
        player_stats_query = (
            select(
                player_table.c.player_name,
                func.count(goal_table.c.id.distinct()).label("total_goals"),
                func.count(case((card_table.c.card_type == 'y', card_table.c.id), else_=None).distinct()).label(
                    "yellow_cards"),
                func.count(case((card_table.c.card_type == 'y2', card_table.c.id), else_=None).distinct()).label(
                    "yellow_red_cards"),
                func.count(case((card_table.c.card_type == 'r', card_table.c.id), else_=None).distinct()).label(
                    "red_cards"),
            )
            .select_from(
                player_table.outerjoin(goal_table, player_table.c.player_api_id == goal_table.c.scorer).outerjoin(
                    card_table, player_table.c.player_api_id == card_table.c.player))
            .where(player_table.c.player_api_id == player_api_id)
            .group_by(player_table.c.player_name)
            .order_by(player_table.c.player_name)
        )

        player_stats_results = await database.fetch_one(player_stats_query)

        home_player_cols = [match_table.c[f"home_player_{i}"] for i in range(1, 12)]
        away_player_cols = [match_table.c[f"away_player_{i}"] for i in range(1, 12)]
        all_player_cols = home_player_cols + away_player_cols

        player_total_matches_query = select(func.count()).select_from(match_table).where(
            or_(
                *[col == player_api_id for col in all_player_cols],

            )
        )

        player_total_matches_result = await database.fetch_one(player_total_matches_query)
        count = player_total_matches_result[0]

        if player_stats_results is None:
            return None

        ret_dict = {"total_matches": count}
        ret_dict.update(dict(player_stats_results))

        return ret_dict
