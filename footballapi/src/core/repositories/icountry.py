"""Module containing country repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class ICountryRepository(ABC):
    """An abstract class representing protocol of country repository."""

    @abstractmethod
    async def get_all_countries(self) -> Iterable[Any]:
        """The abstract getting all countries from the data storage.

        Returns:
            Iterable[Any]: Countries in the data storage.
        """

    @abstractmethod
    async def get_by_name(self, name: str) -> Any | None:
        """The abstract getting a country by its name.

        Args:
            name (str): The name of the country.

        Returns:
            Any | None: The country details.
        """

    @abstractmethod
    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a country by provided id.

        Args:
            id (int): The id of the country.

        Returns:
            Any | None: The country details.
        """

