"""Module containing goal repository implementation."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from sqlalchemy import select, join
from sqlalchemy.orm import aliased

from src.core.domain.goal import Goal
from src.core.repositories.igoal import IGoalRepository
from src.db import goal_table, player_table, database
from src.infrastructure.dto.goaldto import GoalDTO


class GoalRepository(IGoalRepository):
    """An abstract class representing protocol of goal repository."""

    async def get_all_goals(self) -> Iterable[Any]:
        """The abstract getting all goals from the data storage.

        Returns:
            Iterable[Any]: Countries in the data storage.
        """
        query = goal_table.select()
        cards = await database.fetch_all(query)
        return [Goal(**dict(card)) for card in cards]

    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting goals scored in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Goals scored in a match.
        """
        scorer_alias = aliased(player_table)
        assister_alias = aliased(player_table)

        query = (
            select(goal_table, scorer_alias, assister_alias).where(
                goal_table.c.match_id == match_id
            )
            .select_from(
                join(
                    goal_table, scorer_alias,
                    goal_table.c.scorer == scorer_alias.c.player_api_id
                ).outerjoin(
                    assister_alias,
                    goal_table.c.assister == assister_alias.c.player_api_id
                )
            ).order_by(goal_table.c.elapsed)
        )

        #print(str(query))
        goals = await database.fetch_all(query)
        return [GoalDTO.from_record(goal) for goal in goals]



    async def get_by_scorer(self, scorer: int) -> Iterable[Any]:
        """The abstract getting goals scored by a player.

        Args:
            scorer (int): The player_api_id of the player who scored a goal.

        Returns:
            Iterable[Any]: Every goal scored by a player.
        """
        scorer_alias = aliased(player_table)
        assister_alias = aliased(player_table)

        query = (
            select(goal_table, scorer_alias, assister_alias).where(
                goal_table.c.scorer == scorer
            )
            .select_from(
                join(
                    goal_table, scorer_alias,
                    goal_table.c.scorer == scorer_alias.c.player_api_id
                ).outerjoin(
                    assister_alias,
                    goal_table.c.assister == assister_alias.c.player_api_id
                )
            ).order_by(goal_table.c.elapsed)
        )
        goals = await database.fetch_all(query)
        return [GoalDTO.from_record(goal) for goal in goals]

    async def get_by_assister(self, assister: int) -> Iterable[Any]:
        """The abstract getting goals a player helped score.

        Args:
            assister (int): The player_api_id of the player who assisted in scoring a goal.

        Returns:
            Iterable[Any]: Every goal that a player helped score.
        """
        scorer_alias = aliased(player_table)
        assister_alias = aliased(player_table)

        query = (
            select(goal_table, scorer_alias, assister_alias).where(
                goal_table.c.scorer == assister
            )
            .select_from(
                join(
                    goal_table, scorer_alias,
                    goal_table.c.scorer == scorer_alias.c.player_api_id
                ).outerjoin(
                    assister_alias,
                    goal_table.c.assister == assister_alias.c.player_api_id
                )
            ).order_by(goal_table.c.elapsed)
        )
        goals = await database.fetch_all(query)
        return [GoalDTO.from_record(goal) for goal in goals]

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a goal by provided id.

        Args:
            id (int): The id of the goal.

        Returns:
            Any | None: The goal details.
        """
        scorer_alias = aliased(player_table)
        assister_alias = aliased(player_table)

        query = (
            select(goal_table, scorer_alias, assister_alias).where(
                goal_table.c.id == id
            )
            .select_from(
                join(
                    goal_table, scorer_alias,
                    goal_table.c.scorer == scorer_alias.c.player_api_id
                ).outerjoin(
                    assister_alias,
                    goal_table.c.assister == assister_alias.c.player_api_id
                )
            )
        )
        goal = await database.fetch_one(query)
        return GoalDTO.from_record(goal)


