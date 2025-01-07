"""Module containing team repository implementation."""

from typing import Any, Iterable

from src.core.repositories.iteam import ITeamRepository
from src.db import team_table, database
from src.infrastructure.dto.teamdto import TeamDTO


class TeamRepository(ITeamRepository):
    """A class implementing protocol of team repository."""

    async def get_all_teams(self) -> Iterable[Any]:
        """The abstract getting all teams from the data storage.

        Returns:
            Iterable[Any]: Teams in the data storage.
        """

        query = team_table.select()
        teams = await database.fetch_all(query)
        return [TeamDTO.from_record(team) for team in teams]

    async def get_by_team_api_id(self, team_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_api_id.

        Args:
            team_api_id (int): The api_id of the team.

        Returns:
            Any | None: The team details.
        """
        query = team_table.select().where(team_table.c.team_api_id == team_api_id)
        team = await database.fetch_one(query)

        return TeamDTO.from_record(team)

    async def get_by_team_fifa_api_id(self, team_fifa_api_id: int) -> Any | None:
        """The abstract getting a team by provided team_fifa_api_id.

        Args:
            team_fifa_api_id (int): The fifa_api_id of the team. Useful only for attributes

        Returns:
            Any | None: The team details.
        """
        query = team_table.select().where(team_table.c.team_fifa_api_id == team_fifa_api_id)
        team = await database.fetch_one(query)

        return TeamDTO.from_record(team)

    async def get_by_team_long_name(self, team_long_name: str) -> Any | None:
        """The abstract getting a player by provided team_long_name.

        Args:
            team_long_name (str): The name of the team.

        Returns:
            Any | None: The team details.
        """
        query = team_table.select().where(team_table.c.team_long_name == team_long_name)
        team = await database.fetch_one(query)

        return TeamDTO.from_record(team)
