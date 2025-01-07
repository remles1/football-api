"""Module containing league repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class ILeagueRepository(ABC):
    """An abstract class representing protocol of league repository."""

    @abstractmethod
    async def get_all_leagues(self) -> Iterable[Any]:
        """The abstract getting all leagues from the data storage.

        Returns:
            Iterable[Any]: Leagues in the data storage.
        """

    @abstractmethod
    async def get_by_country(self, country_id: int) -> Any | None:
        """The abstract getting a league assigned to a Country.

        Args:
            country_id (int): The id of the country.

        Returns:
            Any | None: The league details.
        """

    @abstractmethod
    async def get_by_name(self, name: str) -> Any | None:
        """The abstract getting a league by its name.

        Args:
            name (str): The name of the league.

        Returns:
            Any | None: The league details.
        """

    @abstractmethod
    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a league by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The league details.
        """
