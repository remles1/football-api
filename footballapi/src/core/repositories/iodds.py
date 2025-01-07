"""Module containing odds repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class IOddsRepository(ABC):
    """An abstract class representing protocol of odds repository."""

    @abstractmethod
    async def get_previous_matches(self, match_api_id: int) -> Iterable[Any]:
        """The abstract getting previous 11 matches
        in a league in the same season. Used for predicting winning odds.

        Args:
            match_api_id (int): match_api_id of the match of which we are predicting odds

        Returns:
            Iterable[Any]: Matches.
        """

