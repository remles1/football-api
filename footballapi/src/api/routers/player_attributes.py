from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.player_attributesdto import PlayerAttributesDTO
from src.infrastructure.services.iplayer_attributes import IPlayerAttributesService

router = APIRouter()


@router.get("/player_api_id/{player_api_id}", response_model=PlayerAttributesDTO, status_code=200)
@inject
async def get_by_player_api_id(player_api_id: int,
                               service: IPlayerAttributesService = Depends(
                                   Provide[Container.player_attributes_service]), ) -> dict:
    """An endpoint for getting Player Attributes by player_api_id.

        Args:
            player_api_id (str): The player_api_id of the player.
            service (IPlayerService): The injected service dependency.

        Raises:
            HTTPException: 404 if there is no player with such player_api_id.

        Returns:
            dict: The requested player attributes.
    """
    if attrs := await service.get_by_player_api_id(player_api_id):
        return attrs.model_dump()

    raise HTTPException(status_code=404, detail="No such player")

