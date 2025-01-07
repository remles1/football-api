"""Module containing country service implementation."""

from typing import Iterable

from src.core.domain.country import Country
from src.core.repositories.icountry import ICountryRepository
from src.infrastructure.services.icountry import ICountryService


class CountryService(ICountryService):
    """A class implementing the country service."""

    _repository: ICountryRepository

    def __init__(self, repository: ICountryRepository):
        """The initializer of the `country service`.

        Args:
            repository (ICountryRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_countries(self) -> Iterable[Country]:
        """The abstract getting all countries from the repository.

        Returns:
            Iterable[Any]: Collection of all countries.
        """

        return await self._repository.get_all_countries()

    async def get_by_name(self, name: str) -> Country | None:
        """The abstract getting a country by its name from the repository.

        Args:
            name (str): The name of the country.

        Returns:
            Any | None: The country details if exists.
        """
        return await self._repository.get_by_name(name)

    async def get_by_id(self, id: int) -> Country | None:
        """The abstract getting a card by provided id from the repository.

        Args:
            id (int): The id of the country.

        Returns:
            Any | None: The country details if exists.
        """
        return await self._repository.get_by_id(id)