"""Module containing card repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.repositories.icountry import ICountryRepository
from src.db import country_table, database

from src.infrastructure.dto.countrydto import CountryDTO


class CountryRepository(ICountryRepository):
    """A class implementing the database country repository."""

    async def get_all_countries(self) -> Iterable[Any]:
        """The abstract getting all countries from the data storage.

        Returns:
            Iterable[Any]: Countries in the data storage.
        """
        query = country_table.select()
        countries = await database.fetch_all(query)

        return [CountryDTO.from_record(country) for country in countries]

    async def get_by_name(self, name: str) -> Any | None:
        """The abstract getting a country by its name.

        Args:
            name (str): The name of the country.

        Returns:
            Any | None: The country details.
        """
        query = country_table.select().where(country_table.c.name == name)
        country = await database.fetch_one(query)

        return CountryDTO.from_record(country)

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a country by provided id.

        Args:
            id (int): The id of the country.

        Returns:
            Any | None: The country details.
        """
        query = country_table.select().where(country_table.c.id == id)
        country = await database.fetch_one(query)

        return CountryDTO.from_record(country)
