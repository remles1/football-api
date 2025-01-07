"""Module containing goal repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class IGoalRepository(ABC):
    """An abstract class representing protocol of goal repository."""

    @abstractmethod
    async def get_all_goals(self) -> Iterable[Any]:
        """The abstract getting all goals from the data storage.

        Returns:
            Iterable[Any]: Goals in the data storage.
        """

    @abstractmethod
    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting goals scored in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Goals scored in a match.
        """

    @abstractmethod
    async def get_by_scorer(self, scorer: int) -> Iterable[Any]:
        """The abstract getting goals scored by a player.

        Args:
            scorer (int): The player_api_id of the player who scored a goal.

        Returns:
            Iterable[Any]: Every goal scored by a player.
        """

    @abstractmethod
    async def get_by_assister(self, assister: int) -> Iterable[Any]:
        """The abstract getting goals a player helped score.

        Args:
            assister (int): The player_api_id of the player who assisted in scoring a goal.

        Returns:
            Iterable[Any]: Every goal that a player helped score.
        """

    @abstractmethod
    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a goal by provided id.

        Args:
            id (int): The id of the goal.

        Returns:
            Any | None: The goal details.
        """


