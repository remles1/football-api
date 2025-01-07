"""Module containing Player Attributes repository implementation."""

from typing import Any

from src.core.repositories.iplayer_attributes import IPlayerAttributesRepository
from src.db import database, player_attributes_table
from src.infrastructure.dto.player_attributesdto import PlayerAttributesDTO


class PlayerAttributesRepository(IPlayerAttributesRepository):
    """A class implementing database protocol of Player Attributes repository."""

    async def get_by_player_api_id(self, player_api_id: int) -> Any | None:
        """The abstract getting players attributes by their player_api_id.

        Args:
            player_api_id (int): The player_api_id of the player.

        Returns:
            Any | None: The players attributes.
        """
        query = player_attributes_table.select().where(player_attributes_table.c.player_api_id == player_api_id).order_by(player_attributes_table.c.date.desc())
        result = await database.fetch_one(query)
        return PlayerAttributesDTO.from_record(result)
