"""Module containing odds service abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class IOddsService(ABC):
    """An abstract class representing protocol of odds services."""

    @abstractmethod
    async def get_previous_matches(self, match_api_id: int) -> Iterable[Any]:
        """The abstract getting previous 20 matches tops
        in a league in the same season. Used for predicting winning odds.

        Args:
            match_api_id (int): match_api_id of the match of which we are predicting odds

        Returns:
            Iterable[Any]: Matches.
        """
