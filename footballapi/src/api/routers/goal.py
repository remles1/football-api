"""A module containing country endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.goal import Goal
from src.infrastructure.dto.goaldto import GoalDTO
from src.infrastructure.services.igoal import IGoalService

router = APIRouter()


@router.get("/all", response_model=Iterable[Goal], status_code=200)
@inject
async def get_all_goals(
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all goals. (HUGE AMOUNT)

    Args:
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: The goal attributes collection.
    """

    if goals := await service.get_all_goals():
        return goals

    raise HTTPException(status_code=404, detail="Goals not found")


@router.get("/match/{match_id}", response_model=Iterable[GoalDTO], status_code=200)
@inject
async def get_goals_by_match(
        match_id: int,
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all goals by match_id.

    Args:
        match_id (int): The id of the match.
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: GoalDTO collection.
    """

    if goals := await service.get_by_match(match_id=match_id):
        return goals

    raise HTTPException(status_code=404, detail="Goals not found")


@router.get("/scorer/{scorer}", response_model=Iterable[GoalDTO], status_code=200)
@inject
async def get_goals_by_scorer(
        scorer: int,
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all goals by scorer.

    Args:
        scorer (int): The player_api_id of the scorer.
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: GoalDTO collection.
    """

    if goals := await service.get_by_scorer(scorer):
        return goals

    raise HTTPException(status_code=404, detail="Goals not found")


@router.get("/assister/{assister}", response_model=Iterable[GoalDTO], status_code=200)
@inject
async def get_goals_by_assister(
        assister: int,
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all goals player helped score.

    Args:
        assister (int): The player_api_id of the assister.
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: GoalDTO collection.
    """

    if goals := await service.get_by_assister(assister):
        return goals

    raise HTTPException(status_code=404, detail="Goals not found")


@router.get("/id/{id}", response_model=GoalDTO, status_code=200)
@inject
async def get_goals_by_id(
        id: int,
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting a goal by its id.

    Args:
        id (int): The id of the goal.
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: GoalDTO collection.
    """

    if goal := await service.get_by_id(id=id):
        return goal.model_dump()

    raise HTTPException(status_code=404, detail="Goal not found")
