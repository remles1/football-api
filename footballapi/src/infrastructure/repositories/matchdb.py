"""Module containing match repository implementation."""

from typing import Any, Iterable

from sqlalchemy import or_

from src.core.repositories.imatch import IMatchRepository
from src.db import match_table, database
from src.infrastructure.dto.matchdto import MatchDTO


class MatchRepository(IMatchRepository):
    """A class implementing database protocol of match repository."""

    async def get_all_matches(self) -> Iterable[Any]:
        """Getting all matches from the data storage. (a lot)

        Returns:
            Iterable[Any]: Matches in the data storage.
        """
        from src.container import Container

        query = match_table.select()  # .limit(3)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_league_id(self, league_id: int) -> Iterable[Any]:
        """The abstract getting matches played in a league.

        Args:
            league_id (int): The id of the league.

        Returns:
            Iterable[Any]: Matches played in a league.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.league_id == league_id)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_season(self, season: str) -> Iterable[Any]:
        """The abstract getting matches played in a season.

        Args:
            season (str): The season in the format "YYYY/YYYY".

        Returns:
            Iterable[Any]: Matches played in a season.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.season == season)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_date(self, date: str) -> Iterable[Any]:
        """The abstract getting matches played on a certain date.

        Args:
            date (str): The date in the format "YYYY-MM-DD".

        Returns:
            Iterable[Any]: Matches played on a certain date.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.date == date)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_match_api_id(self, match_api_id: int) -> Any | None:
        """The abstract getting a match by a provided match_api_id.

        Args:
            match_api_id (int): The id of a match

        Returns:
            Any | None: Match fetched by its id.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.match_api_id == match_api_id)
        match = await database.fetch_one(query)

        return await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                          goal_repo_interface=Container.goal_repository())

    async def get_by_team_api_id(self, team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided team_api_id.

        Args:
            team_api_id (int): The id of the team.

        Returns:
            Iterable[Any]: Matches played by a certain team.
        """
        from src.container import Container

        query = match_table.select().where(
            or_(
                match_table.c.home_team_api_id == team_api_id,
                match_table.c.away_team_api_id == team_api_id
            )
        )
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_home_team(self, home_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided home_team_api_id.

        Args:
            home_team_api_id (int): The id of the home team.

        Returns:
            Iterable[Any]: Matches played by a certain team in home.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.home_team_api_id == home_team_api_id)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_away_team(self, away_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided away_team_api_id.

        Args:
            away_team_api_id (int): The id of the away team.

        Returns:
            Iterable[Any]: Matches played by a certain team away.
        """
        from src.container import Container

        query = match_table.select().where(match_table.c.away_team_api_id == away_team_api_id)
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]

    async def get_by_player_api_id(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id.

        Args:
            player_api_id (int): The id of the player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field.
        """
        from src.container import Container

        home_player_cols = [match_table.c[f"home_player_{i}"] for i in range(1, 12)]
        away_player_cols = [match_table.c[f"away_player_{i}"] for i in range(1, 12)]
        all_player_cols = home_player_cols + away_player_cols

        query = match_table.select().where(or_(*[col == player_api_id for col in all_player_cols]))
        matches = await database.fetch_all(query)

        return [await MatchDTO.from_record(record=match, card_repo_interface=Container.card_repository(),
                                           goal_repo_interface=Container.goal_repository()) for match in matches]
