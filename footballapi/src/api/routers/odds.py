from typing import Iterable

import simplejson as json
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.infrastructure.dto.oddsdto import OddsDTO
from src.infrastructure.services.iodds import IOddsService

router = APIRouter()


@router.get("/{match_api_id}", response_model=OddsDTO, status_code=200)
@inject
async def get_odds(match_api_id: int,
                   service: IOddsService = Depends(Provide[Container.odds_service]), ) -> Iterable:
    """An endpoint for getting win likelihood of a match by its match_api_id.

        Args:
            match_api_id (int): The match_api_id of the match.
            service (IOddsService): The injected service dependency.

        Raises:
            HTTPException: 404 if there is no match with such match_api_id.

        Returns:
            dict: The requested team attributes.
    """
    previous_matches = await service.get_previous_matches(match_api_id)
    if previous_matches is None:
        raise HTTPException(status_code=404, detail="No such match")
    # print(previous_matches_dict)
    previous_matches_dict = [dict(record) for record in previous_matches]
    data_json = json.dumps(previous_matches_dict, use_decimal=True)

    if result := await Container.rpc_client().call(data_json):
        return result

    # if temp := await service.get_previous_matches(match_api_id):
    #     return temp

    #raise HTTPException(status_code=404, detail="No such match")
