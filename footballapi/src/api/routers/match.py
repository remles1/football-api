"""A module containing card endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.matchdto import MatchDTO
from src.infrastructure.services.imatch import IMatchService

router = APIRouter()


@router.get("/all", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_all_matches(
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable:
    """An endpoint for getting all matches.

    Args:
        service (IMatchService): The injected service dependency.

    Returns:
        Iterable: All matches in the database.
    """

    matches = await service.get_all_matches()

    return matches


@router.get("/league/{league_id}", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_by_league_id(
        league_id: int,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable:
    """An endpoint for getting all matches in a specific league.

    Args:
        league_id (int): The id of the league.
        service (IMatchService): The injected service dependency.

    Returns:
        Iterable: All matches in the specified league.
    """

    if matches := await service.get_by_league_id(league_id=league_id):
        return matches

    raise HTTPException(status_code=404, detail="Matches not found")


@router.get("/season/{season}", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_by_season(
        season: str,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable:
    """An endpoint for getting all matches in a specific season.

    Args:
        season (str): The season in the format "YYYY-YYYY".
        service (IMatchService): The injected service dependency.

    Returns:
        Iterable: All matches in the specified league.
    """
    season = season.replace("-", "/")
    if matches := await service.get_by_season(season=season):
        return matches

    raise HTTPException(status_code=404, detail="Matches not found")


@router.get("/date/{date}", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_by_date(
        date: str,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable:
    """An endpoint for getting all matches played on a specific date.

    Args:
        date (str): The date in the format "YYYY-MM-DD".
        service (IMatchService): The injected service dependency.

    Returns:
        Iterable: All matches on the specified date.
    """
    date = date + " 00:00:00"
    if matches := await service.get_by_date(date=date):
        return matches

    raise HTTPException(status_code=404, detail="Matches not found")


@router.get("/match_api_id/{match_api_id}", response_model=MatchDTO, status_code=200)
@inject
async def get_by_match_api_id(
        match_api_id: int,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> MatchDTO:
    """An endpoint for getting a match by match_api_id.

    Args:
        match_api_id (int): Match api id.
        service (IMatchService): The injected service dependency.

    Returns:
        MatchDTO: The matched match.
    """

    if match := await service.get_by_match_api_id(match_api_id=match_api_id):
        return match.model_dump()

    raise HTTPException(status_code=404, detail="Match not found")


@router.get("/team_api_id/{team_api_id}", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_by_team_api_id(
        team_api_id: int,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable[MatchDTO]:
    """The abstract getting a match by a provided team_api_id.

    Args:
        team_api_id (int): The id of the team.
        service (IMatchService): The injected service dependency.
    Returns:
        Iterable[Any]: Matches played by a certain team.
    """

    if matches := await service.get_by_team_api_id(team_api_id):
        return matches

    raise HTTPException(status_code=404, detail="Matches not found")


@router.get("/player_api_id/{player_api_id}", response_model=Iterable[MatchDTO], status_code=200)
@inject
async def get_by_team_api_id(
        player_api_id: int,
        service: IMatchService = Depends(Provide[Container.match_service]),
) -> Iterable[MatchDTO]:
    """The abstract getting matches a player with player_api_id played in.

    Args:
        player_api_id (int): The id of the player.
        service (IMatchService): The injected service dependency.
    Returns:
        Iterable[Any]: Matches played by a certain team.
    """

    if matches := await service.get_by_player_api_id(player_api_id):
        return matches

    raise HTTPException(status_code=404, detail="Matches not found")
