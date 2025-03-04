"""A module containing team endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.teamdto import TeamDTO
from src.infrastructure.services.iteam import ITeamService

router = APIRouter()


@router.get("/all", response_model=Iterable[TeamDTO], status_code=200)
@inject
async def get_all_teams(
        service: ITeamService = Depends(Provide[Container.team_service]),
) -> Iterable:
    """An endpoint for getting all teams.

    Args:
        service (ITeamService, optional): The injected service dependency.

    Returns:
        Iterable: The team collection.
    """
    teams = await service.get_all_teams()
    return teams


@router.get("/team_api_id/{team_api_id}", response_model=TeamDTO, status_code=200)
@inject
async def get_by_team_api_id(
        team_api_id: int,
        service: ITeamService = Depends(Provide[Container.team_service]),
) -> dict:
    """An endpoint for getting team details by team_api_id.

    Args:
        team_api_id (int): team_api_id field of the Team
        service (ITeamService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if team does not exist.

    Returns:
        dict: The requested team attributes.
    """
    if team := await service.get_by_team_api_id(team_api_id):
        return team.model_dump()

    raise HTTPException(status_code=404, detail="Team not found")


@router.get("/team_fifa_api_id/{team_fifa_api_id}", response_model=TeamDTO, status_code=200)
@inject
async def get_by_team_fifa_api_id(
        team_fifa_api_id: int,
        service: ITeamService = Depends(Provide[Container.team_service]),
) -> dict:
    """An endpoint for getting team details by team_fifa_api_id.

    Args:
        team_fifa_api_id (int): The team_fifa_api_id of the Team.
        service (ITeamService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if team does not exist.

    Returns:
        dict: The requested team attributes.
    """

    if team := await service.get_by_team_fifa_api_id(team_fifa_api_id):
        return team.model_dump()

    raise HTTPException(status_code=404, detail="Team not found")


@router.get("/team_long_name/{team_long_name}", response_model=TeamDTO, status_code=200)
@inject
async def get_by_team_long_name(
        team_long_name: str,
        service: ITeamService = Depends(Provide[Container.team_service]),
) -> dict:
    """An endpoint for getting team details by team_fifa_api_id.

    Args:
        team_long_name (str): The full name of the Team.
        service (ITeamService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if team does not exist.

    Returns:
        dict: The requested team attributes.
    """

    if team := await service.get_by_team_long_name(team_long_name):
        return team.model_dump()

    raise HTTPException(status_code=404, detail="Team not found")


@router.get("/stats/{team_api_id}", response_model=dict, status_code=200)
@inject
async def get_stats(
        team_api_id: int,
        service: ITeamService = Depends(Provide[Container.team_service]),
) -> dict:
    """The abstract getting team statistics by provided team_api_id.

    Args:
        team_api_id (int): The team_api_id of the team.
        service (ITeamService, optional): The injected service dependency.

    Returns:
        Any | None: The requested stats.
    """

    if stats := await service.get_stats(team_api_id):
        return stats

    raise HTTPException(status_code=404, detail="Team not found")
