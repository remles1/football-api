"""A module containing league endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.leaguedto import LeagueDTO
from src.infrastructure.services.ileague import ILeagueService

router = APIRouter()


@router.get("/all", response_model=Iterable[LeagueDTO], status_code=200)
@inject
async def get_all_leagues(
        service: ILeagueService = Depends(Provide[Container.league_service]),
) -> Iterable:
    """An endpoint for getting all leagues.

    Args:
        service (ILeagueService): The injected service dependency.

    Returns:
        Iterable: All leagues in the database.
    """

    leagues = await service.get_all_leagues()
    return leagues


@router.get("/country/{country_id}", response_model=LeagueDTO, status_code=200)
@inject
async def get_by_country(
        country_id: int,
        service: ILeagueService = Depends(Provide[Container.league_service]),
) -> dict:
    """An endpoint for getting league details by id.

    Args:
        country_id (int): The id of the country.
        service (ILeagueService): The injected service dependency.

    Raises:
        HTTPException: 404 if there isn't a league in a country, or there is no country.

    Returns:
        LeagueDTO: The requested league DTO.
    """

    if league := await service.get_by_country(country_id):
        return league.model_dump()

    raise HTTPException(status_code=404, detail="League not found")


@router.get("/name/{name}", response_model=LeagueDTO, status_code=200)
@inject
async def get_by_name(
        name: str,
        service: ILeagueService = Depends(Provide[Container.league_service]),
) -> dict:
    """An endpoint for getting league details by id.

    Args:
        name (str): The name of the league.
        service (ILeagueService): The injected service dependency.

    Raises:
        HTTPException: 404 if there isn't a league with such name.

    Returns:
        LeagueDTO: The requested league DTO.
    """

    if league := await service.get_by_name(name):
        return league.model_dump()

    raise HTTPException(status_code=404, detail="League not found")


@router.get("/id/{id}", response_model=LeagueDTO, status_code=200)
@inject
async def get_by_id(
        id: int,
        service: ILeagueService = Depends(Provide[Container.league_service]),
) -> dict:
    """An endpoint for getting league details by id.

    Args:
        id (int): The id of the league.
        service (ILeagueService): The injected service dependency.

    Raises:
        HTTPException: 404 if there is no league with such id.

    Returns:
        LeagueDTO: The requested league DTO.
    """

    if league := await service.get_by_id(id):
        return league.model_dump()

    raise HTTPException(status_code=404, detail="League not found")


@router.get("/stats/{id}", response_model=dict, status_code=200)
@inject
async def stats(
        id: int,
        service: ILeagueService = Depends(Provide[Container.league_service]),
) -> dict:
    """An endpoint for getting stats of a league by its id.

    Args:
        id (int): The id of the league.
        service (ILeagueService): The injected service dependency.

    Raises:
        HTTPException: 404 if there is no league with such id.

    Returns:
        dict: The requested stats.
    """

    if stats_dict := await service.stats(id):
        return stats_dict

    raise HTTPException(status_code=404, detail="League not found")
