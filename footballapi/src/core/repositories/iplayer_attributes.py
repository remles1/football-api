"""Module containing player attributes repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any


class IPlayerAttributesRepository(ABC):
    """An abstract class representing protocol of league repository."""

    @abstractmethod
    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting players attributes by their player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The players attributes.
        """

