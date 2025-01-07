"""Module containing Team Attributes repository implementation."""

from typing import Any

from src.core.repositories.iteam_attributes import ITeamAttributesRepository
from src.db import database, team_attributes_table
from src.infrastructure.dto.team_attributesdto import TeamAttributesDTO


class TeamAttributesRepository(ITeamAttributesRepository):
    """A class implementing database protocol of Team Attributes repository."""

    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a teams attributes by its team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The teams attributes.
        """
        query = team_attributes_table.select().where(team_attributes_table.c.team_api_id == team_api_id).order_by(team_attributes_table.c.date.desc())
        result = await database.fetch_one(query)
        return TeamAttributesDTO.from_record(result)
