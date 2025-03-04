"""Module containing league service implementations."""

from typing import Any, Iterable

from src.core.repositories.ileague import ILeagueRepository
from src.infrastructure.services.ileague import ILeagueService


class LeagueService(ILeagueService):
    """A class implementing protocol of league service."""

    _repository: ILeagueRepository

    def __init__(self, repository: ILeagueRepository):
        """The initializer of the `card service`.

            Args:
                repository (ILeagueService): The reference to the repository.
            """
        self._repository = repository

    async def get_all_leagues(self) -> Iterable[Any]:
        """The abstract getting all leagues from the data storage.

        Returns:
            Iterable[Any]: Leagues in the data storage.
        """
        return await self._repository.get_all_leagues()

    async def get_by_country(self, country_id: int) -> Any | None:
        """The abstract getting a league assigned to a Country.

        Args:
            country_id (int): The id of the country.

        Returns:
            Any | None: The league details.
        """
        return await self._repository.get_by_country(country_id)

    async def get_by_name(self, name: str) -> Any | None:
        """The abstract getting a league by its name.

        Args:
            name (str): The name of the league.

        Returns:
            Any | None: The league details.
        """
        return await self._repository.get_by_name(name)

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a league by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The league details.
        """
        return await self._repository.get_by_id(id)

    async def stats(self, id: int) -> Any | None:
        """The abstract getting a league statistics by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The requested stats.
        """
        return await self._repository.stats(id)