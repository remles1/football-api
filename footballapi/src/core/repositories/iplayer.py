"""Module containing player repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class IPlayerRepository(ABC):
    """An abstract class representing protocol of player repository."""

    @abstractmethod
    async def get_all_players(self) -> Iterable[Any]:
        """The abstract getting all players from the data storage.

        Returns:
            Iterable[Any]: Players in the data storage.
        """

    @abstractmethod
    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting a player by provided player_api_id.

        Args:
            player_api_id (int): The api_id of the player.

        Returns:
            Any | None: The player details.
        """

    @abstractmethod
    async def get_by_player_name(self, player_name: str) -> Any | None:
        """The abstract getting a player by their name.

        Args:
            player_name (str): The name of the player.

        Returns:
            Any | None: The player details.
        """

    @abstractmethod
    async def get_stats(self, player_api_id: int) -> Any | None:
        """The abstract getting a player statistics by provided player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The requested stats.
        """


