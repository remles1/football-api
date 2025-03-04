"""Module containing team service implementation."""

from typing import Any, Iterable

from src.core.repositories.iteam import ITeamRepository
from src.infrastructure.services.iteam import ITeamService


class TeamService(ITeamService):
    """A class implementing protocol of team service."""
    _repository: ITeamRepository

    def __init__(self, repository: ITeamRepository):
        """The initializer of the `team service`.

        Args:
            repository (ITeamRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_teams(self) -> Iterable[Any]:
        """The abstract getting all teams from the data storage.

        Returns:
            Iterable[Any]: Teams in the data storage.
        """
        return await self._repository.get_all_teams()

    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_api_id.

        Args:
            team_api_id (int): The api_id of the team.

        Returns:
            Any | None: The team details.
        """
        return await self._repository.get_by_team_api_id(team_api_id)

    async def get_by_team_fifa_api_id(self, team_fifa_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_fifa_api_id.

        Args:
            team_fifa_api_id (int): The fifa_api_id of the team. Useful only for attributes

        Returns:
            Any | None: The team details.
        """
        return await self._repository.get_by_team_fifa_api_id(team_fifa_api_id)

    async def get_by_team_long_name(self, team_long_name: str) -> Any | None:
        """The abstract getting a player by provided team_long_name.

        Args:
            team_long_name (str): The name of the team.

        Returns:
            Any | None: The team details.
        """
        return await self._repository.get_by_team_long_name(team_long_name)

    async def get_stats(self, team_api_id: int) -> Any | None:
        """The abstract getting team statistics by provided team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The requested stats.
        """
        return await self._repository.get_stats(team_api_id)