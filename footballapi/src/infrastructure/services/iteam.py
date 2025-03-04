"""Module containing team service abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class ITeamService(ABC):
    """An abstract class representing protocol of team service."""

    @abstractmethod
    async def get_all_teams(self) -> Iterable[Any]:
        """The abstract getting all teams from the data storage.

        Returns:
            Iterable[Any]: Teams in the data storage.
        """

    @abstractmethod
    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_api_id.

        Args:
            team_api_id (int): The api_id of the team.

        Returns:
            Any | None: The team details.
        """

    @abstractmethod
    async def get_by_team_fifa_api_id(self, team_fifa_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_fifa_api_id.

        Args:
            team_fifa_api_id (int): The fifa_api_id of the team. Useful only for attributes

        Returns:
            Any | None: The team details.
        """

    @abstractmethod
    async def get_by_team_long_name(self, team_long_name: str) -> Any | None:
        """The abstract getting a team by provided team_long_name.

        Args:
            team_long_name (str): The name of the team.

        Returns:
            Any | None: The team details.
        """

    @abstractmethod
    async def get_stats(self, team_api_id: int) -> Any | None:
        """The abstract getting team statistics by provided team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The requested stats.
        """
