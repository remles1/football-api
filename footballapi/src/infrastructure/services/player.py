"""Module containing player service implementation."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from src.core.repositories.iplayer import IPlayerRepository
from src.infrastructure.services.iplayer import IPlayerService


class PlayerService(IPlayerService):
    """A class implementing the player service."""

    _repository: IPlayerRepository

    def __init__(self, repository: IPlayerRepository):
        """The initializer of the `player service`.

        Args:
            repository (IPlayerRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_players(self) -> Iterable[Any]:
        """The abstract getting all players from the data storage.

        Returns:
            Iterable[Any]: Players in the data storage.
        """
        return await self._repository.get_all_players()

    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting a player by provided player_api_id.

        Args:
            player_api_id (int): The api_id of the player.

        Returns:
            Any | None: The player details.
        """
        return await self._repository.get_by_player_api_id(player_api_id)

    async def get_by_player_name(self, player_name: str) -> Any | None:
        """The abstract getting a player by their name.

        Args:
            player_name (str): The name of the player.

        Returns:
            Any | None: The player details.
        """
        return await self._repository.get_by_player_name(player_name)

    async def get_stats(self, player_api_id: int) -> Any | None:
        """The abstract getting a player statistics by provided player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The requested stats.
        """
        return await self._repository.get_stats(player_api_id)

