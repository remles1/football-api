from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.team_attributesdto import TeamAttributesDTO
from src.infrastructure.services.iteam_attributes import ITeamAttributesService

router = APIRouter()


@router.get("/team_api_id/{team_api_id}", response_model=TeamAttributesDTO, status_code=200)
@inject
async def get_by_team_api_id(team_api_id: int,
                             service: ITeamAttributesService = Depends(Provide[Container.team_attributes_service]), ) -> dict:
    """An endpoint for getting Team Attributes by team_api_id.

        Args:
            team_api_id (str): The team_api_id of the team.
            service (ITeamAttributesService): The injected service dependency.

        Raises:
            HTTPException: 404 if there is no team with such player_api_id.

        Returns:
            dict: The requested team attributes.
    """
    if attrs := await service.get_by_team_api_id(team_api_id):
        return attrs.model_dump()

    raise HTTPException(status_code=404, detail="No such team")

