"""Module containing country service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.country import Country


class ICountryService(ABC):
    """An abstract class representing protocol of country service"""

    @abstractmethod
    async def get_all_countries(self) -> Iterable[Country]:
        """The abstract getting all countries from the repository.

        Returns:
            Iterable[Any]: Collection of all countries.
        """

    @abstractmethod
    async def get_by_name(self, name: str) -> Country | None:
        """The abstract getting a country by its name from the repository.

        Args:
            name (str): The name of the country.

        Returns:
            Any | None: The country details if exists.
        """

    @abstractmethod
    async def get_by_id(self, id: int) -> Country | None:
        """The abstract getting a card by provided id from the repository.

        Args:
            id (int): The id of the card.

        Returns:
            Any | None: The country details if exists.
        """
