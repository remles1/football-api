"""Module containing Team Attributes service implementation."""

from typing import Any

from src.core.repositories.iteam_attributes import ITeamAttributesRepository
from src.infrastructure.services.iteam_attributes import ITeamAttributesService


class TeamAttributesService(ITeamAttributesService):
    """A class implementing protocol of card service."""

    _repository: ITeamAttributesRepository

    def __init__(self, repository: ITeamAttributesRepository):
        """The initializer of the `Team Attributes service`.

            Args:
                repository (ITeamAttributesRepository): The reference to the repository.
            """
        self._repository = repository

    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a teams attributes by its team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The player's attributes.
        """
        return await self._repository.get_by_team_api_id(team_api_id)
