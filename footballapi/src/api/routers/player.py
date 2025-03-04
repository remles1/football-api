"""A module containing player endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.playerdto import PlayerDTO
from src.infrastructure.services.iplayer import IPlayerService

router = APIRouter()


@router.get("/all", response_model=Iterable[PlayerDTO], status_code=200)
@inject
async def get_all_players(
        service: IPlayerService = Depends(Provide[Container.player_service]),
) -> Iterable:
    """An endpoint for getting all players.

    Args:
        service (IPlayerService): The injected service dependency.

    Returns:
        Iterable: The player collection.
    """
    players = await service.get_all_players()
    return players


@router.get("/player_api_id/{player_api_id}", response_model=PlayerDTO, status_code=200)
@inject
async def get_by_player_api_id(
        player_api_id: int,
        service: IPlayerService = Depends(Provide[Container.player_service]),
) -> dict:
    """An endpoint for getting player details by player_api_id.

    Args:
        player_api_id (int): The player_api_id of the player.
        service (IPlayerService): The injected service dependency.

    Raises:
        HTTPException: 404 if there are no players with such player_api_id.

    Returns:
        dict: The requested player.
    """

    if player := await service.get_by_player_api_id(player_api_id):
        return player.model_dump()

    raise HTTPException(status_code=404, detail="Player not found")


@router.get("/player_name/{player_name}", response_model=Iterable[PlayerDTO], status_code=200)
@inject
async def get_by_player_name(
        player_name: str,
        service: IPlayerService = Depends(Provide[Container.player_service]),
) -> Iterable[PlayerDTO]:
    """An endpoint for getting player details by player_api_id.

    Args:
        player_name (str): The name of the player.
        service (IPlayerService): The injected service dependency.

    Raises:
        HTTPException: 404 if there are no players with such player_api_id.

    Returns:
        dict: The requested player.
    """

    if players := await service.get_by_player_name(player_name):
        return players

    raise HTTPException(status_code=404, detail="Player/Players not found")


@router.get("/stats/{player_api_id}", response_model=dict, status_code=200)
@inject
async def get_stats(
        player_api_id: int,
        service: IPlayerService = Depends(Provide[Container.player_service]),
) -> dict:
    """An endpoint for getting stats of a player by theirs player_api_id.

    Args:
        player_api_id (int): The api id of the player.
        service (ILeagueService): The injected service dependency.

    Raises:
        HTTPException: 404 if there is no league with such id.

    Returns:
        dict: The requested stats.
    """

    if stats_dict := await service.get_stats(player_api_id):
        return stats_dict

    raise HTTPException(status_code=404, detail="Player not found")
