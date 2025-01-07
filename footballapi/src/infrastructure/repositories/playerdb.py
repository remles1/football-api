"""Module containing player repository abstractions."""

from typing import Any, Iterable

from src.core.repositories.iplayer import IPlayerRepository
from src.db import player_table, database
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
        result = await database.fetch_one(query)
        return PlayerDTO.from_record(result)
