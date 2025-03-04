"""Module containing goal service implementation."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from src.core.repositories.igoal import IGoalRepository
from src.infrastructure.services.igoal import IGoalService


class GoalService(IGoalService):
    """A class representing protocol of goal service."""

    _repository: IGoalRepository

    def __init__(self, repository: IGoalRepository):
        """The initializer of the `goal service`.

        Args:
            repository (IGoalRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_goals(self) -> Iterable[Any]:
        """The abstract getting all goals from the data storage.

        Returns:
            Iterable[Any]: Countries in the data storage.
        """
        return await self._repository.get_all_goals()

    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting goals scored in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Goals scored in a match.
        """
        return await self._repository.get_by_match(match_id)

    async def get_by_scorer(self, scorer: int) -> Iterable[Any]:
        """The abstract getting goals scored by a player.

        Args:
            scorer (int): The player_api_id of the player who scored a goal.

        Returns:
            Iterable[Any]: Every goal scored by a player.
        """
        return await self._repository.get_by_scorer(scorer)

    async def get_by_assister(self, assister: int) -> Iterable[Any]:
        """The abstract getting goals a player helped score.

        Args:
            assister (int): The player_api_id of the player who assisted in scoring a goal.

        Returns:
            Iterable[Any]: Every goal that a player helped score.
        """
        return await self._repository.get_by_assister(assister)

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a goal by provided id.

        Args:
            id (int): The id of the goal.

        Returns:
            Any | None: The goal details.
        """
        return await self._repository.get_by_id(id)

