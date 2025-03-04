"""Module containing team repository implementation."""

from typing import Any, Iterable

from sqlalchemy import select, func, join, or_, and_

from src.core.repositories.iteam import ITeamRepository
from src.db import team_table, database, match_table
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

    async def get_stats(self, team_api_id: int) -> Any | None:
        """The abstract getting team statistics by provided team_api_id.

        Args:
            team_api_id (int): The team_api_id of the team.

        Returns:
            Any | None: The requested stats.
        """
        total_games_played_query = select(
            func.count().label("total_games_played")
        ).where(
            or_(
                match_table.c.home_team_api_id == team_api_id,
                match_table.c.away_team_api_id == team_api_id
            )
        )

        total_games_played_result = await database.fetch_one(total_games_played_query)

        wins_home_query = select(
            func.count().label("wins_home")
        ).select_from(
            join(team_table, match_table, team_api_id == match_table.c.home_team_api_id)
        ).where(
            and_(
                match_table.c.home_team_goal > match_table.c.away_team_goal,
                team_table.c.team_api_id == team_api_id
            )
        )

        wins_away_query = select(
            func.count().label("wins_away")
        ).select_from(
            join(team_table, match_table, team_api_id == match_table.c.away_team_api_id)
        ).where(
            and_(
                match_table.c.away_team_goal > match_table.c.home_team_goal,
                team_table.c.team_api_id == team_api_id
            )
        )

        wins_home_result = await database.fetch_one(wins_home_query)
        wins_away_result = await database.fetch_one(wins_away_query)

        ret_dict = dict(total_games_played_result)
        ret_dict.update(wins_home_result)
        ret_dict.update(wins_away_result)

        return ret_dict
