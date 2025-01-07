"""Module containing match repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class IMatchRepository(ABC):
    """An abstract class representing protocol of match repository."""

    @abstractmethod
    async def get_all_matches(self) -> Iterable[Any]:
        """The abstract getting all matches from the data storage.

        Returns:
            Iterable[Any]: Matches in the data storage.
        """

    @abstractmethod
    async def get_by_league_id(self, league_id: int) -> Iterable[Any]:
        """The abstract getting matches played in a league.

        Args:
            league_id (int): The id of the league.

        Returns:
            Iterable[Any]: Matches played in a league.
        """

    @abstractmethod
    async def get_by_season(self, season: str) -> Iterable[Any]:
        """The abstract getting matches played in a season.

        Args:
            season (str): The season in the format "YYYY/YYYY".

        Returns:
            Iterable[Any]: Matches played in a season.
        """

    @abstractmethod
    async def get_by_date(self, date: str) -> Iterable[Any]:
        """The abstract getting matches played on a certain date.

        Args:
            date (str): The date in the format "YYYY-MM-DD".

        Returns:
            Iterable[Any]: Matches played on a certain date.
        """

    @abstractmethod
    async def get_by_match_api_id(self, match_api_id: int) -> Any | None:
        """The abstract getting a match by a provided match_api_id.

        Args:
            match_api_id (int): The id of a match

        Returns:
            Any | None: Match fetched by its id.
        """

    @abstractmethod
    async def get_by_team_api_id(self, team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided team_api_id.

        Args:
            team_api_id (int): The id of the team.

        Returns:
            Iterable[Any]: Matches played by a certain team.
        """

    @abstractmethod
    async def get_by_home_team(self, home_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided home_team_api_id.

        Args:
            home_team_api_id (int): The id of the home team.

        Returns:
            Iterable[Any]: Matches played by a certain team in home.
        """

    @abstractmethod
    async def get_by_away_team(self, away_team_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided away_team_api_id.

        Args:
            away_team_api_id (int): The id of the away team.

        Returns:
            Iterable[Any]: Matches played by a certain team away.
        """

    @abstractmethod
    async def get_by_player_api_id(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id.

        Args:
            player_api_id (int): The id of the player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field.
        """

    @abstractmethod
    async def get_by_home_player(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id playing at home.

        Args:
            player_api_id (int): The id of the home player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field at home.
        """

    @abstractmethod
    async def get_by_away_player(self, player_api_id: int) -> Iterable[Any]:
        """The abstract getting a match by a provided player_api_id playing away.

        Args:
            player_api_id (int): The id of the away player.

        Returns:
            Iterable[Any]: Matches with a certain player in the field away.
        """