"""Module containing odds service implementation."""

from typing import Any, Iterable

from src.core.repositories.iodds import IOddsRepository
from src.infrastructure.services.iodds import IOddsService


class OddsService(IOddsService):
    """A class implementing the odds service."""

    _repository: IOddsRepository

    def __init__(self, repository: IOddsRepository):
        """The initializer of the `odds service`.

        Args:
            repository (IOddsRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_previous_matches(self, match_api_id: int) -> Iterable[Any]:
        """The abstract getting previous 10 matches
        in a league in the same season. Used for predicting winning odds.

        Args:
            match_api_id (int): match_api_id of the match of which we are predicting odds

        Returns:
            Iterable[Any]: Matches.
        """
        return await self._repository.get_previous_matches(match_api_id)
