"""Module containing Player Attributes service implementation."""

from typing import Any

from src.core.repositories.iplayer_attributes import IPlayerAttributesRepository
from src.infrastructure.services.iplayer_attributes import IPlayerAttributesService


class PlayerAttributesService(IPlayerAttributesService):
    """A class implementing protocol of Player Attributes service."""

    _repository: IPlayerAttributesRepository

    def __init__(self, repository: IPlayerAttributesRepository):
        """The initializer of the `Player Attributes service`.

            Args:
                repository (IPlayerAttributesRepository): The reference to the repository.
            """
        self._repository = repository

    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting players attributes by their player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The players attributes.
        """
        return await self._repository.get_by_player_api_id(player_api_id)
