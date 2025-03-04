"""Module containing match service implementation."""

from typing import Any, Iterable

from src.core.repositories.imatch import IMatchRepository
from src.infrastructure.services.imatch import IMatchService


class MatchService(IMatchService):
    """A class implementing the match service."""

    _repository: IMatchRepository

    def __init__(self, repository: IMatchRepository):
        """The initializer of the `country service`.

        Args:
            repository (ICountryRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_matches(self) -> Iterable[Any]:
        """The abstract getting all matches from the data storage.

        Returns:
            Iterable[Any]: Matches in the data storage.
        """
        return await self._repository.get_all_matches()

    async def get_by_league_id(self, league_id: int) -> Iterable[Any]:
        """The abstract getting matches played in a league.

        Args:
            league_id (int): The id of the league.

        Returns:
            Iterable[Any]: Matches played in a league.
        """
        return await self._repository.get_by_league_id(league_id)

    async def get_by_season(self, season: str) -> Iterable[Any]:
        """The abstract getting matches played in a season.

        Args:
            season (str): The season in the format "YYYY/YYYY".

        Returns:
            Iterable[Any]: Matches played in a season.
        """
        return await self._repository.get_by_season(season)

    async def get_by_date(self, date: str) -> Iterable[Any]:
        """The abstract getting matches played on a certain date.

        Args:
            date (str): The date in the format "YYYY-MM-DD".

        Returns:
            Iterable[Any]: Matches played on a certain date.
        """
        return await self._repository.get_by_date(date)

    async def get_by_match_api_id(self, match_api_id: int) -> Any | None:
        """The abstract getting a match by a provided match_api_id.

        Args:
            match_api_id (int): The id of a match

        Returns:
            Any | None: Match fetched by its id.
        """
        return await self._repository.get_by_match_api_id(match_api_id)

    async def get_by_team_api_id(self, team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided team_api_id.

        Args:
            team_api_id (int): The id of the team.

        Returns:
            Iterable[Any]: Matches played by a certain team.
        """
        return await self._repository.get_by_team_api_id(team_api_id)

    async def get_by_home_team(self, home_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided home_team_api_id.

        Args:
            home_team_api_id (int): The id of the home team.

        Returns:
            Iterable[Any]: Matches played by a certain team in home.
        """
        return await self._repository.get_by_home_team(home_team_api_id)

    async def get_by_away_team(self, away_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided away_team_api_id.

        Args:
            away_team_api_id (int): The id of the away team.

        Returns:
            Iterable[Any]: Matches played by a certain team away.
        """
        return await self._repository.get_by_away_team(away_team_api_id)

    async def get_by_player_api_id(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting matches a player with player_api_id played in.

        Args:
            player_api_id (int): The id of the player.
        Returns:
            Iterable[Any]: Matches played by a certain player.
        """
        return await self._repository.get_by_player_api_id(player_api_id)

    async def get_by_home_player(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id playing at home.

        Args:
            player_api_id (int): The id of the home player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field at home.
        """

    async def get_by_away_player(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id playing away.

        Args:
            player_api_id (int): The id of the away player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field away.
        """