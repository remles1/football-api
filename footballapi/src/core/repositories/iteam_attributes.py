"""Module containing Team Attributes repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any


class ITeamAttributesRepository(ABC):
    """An abstract class representing protocol of league repository."""

    @abstractmethod
    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a teams attributes by its team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The player's attributes.
        """
