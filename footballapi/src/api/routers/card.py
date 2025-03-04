"""A module containing card endpoints."""

from typing import Iterable, Any

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.card import Card
from src.infrastructure.dto.carddto import CardDTO
from src.infrastructure.services.icard import ICardService

router = APIRouter()


@router.get("/all", response_model=Iterable[Card], status_code=200)
@inject
async def get_all_cards(
        service: ICardService = Depends(Provide[Container.card_service]),
) -> Iterable:
    """An endpoint for getting all cards.

    Args:
        service (ICountryService): The injected service dependency.

    Returns:
        Iterable: All cards in the database.
    """

    cards = await service.get_all_cards()

    return cards


@router.get("/match/{match_id}", response_model=Iterable[CardDTO], status_code=200)
@inject
async def get_cards_by_match(
        match_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> Iterable:
    """An endpoint for getting card details by id.

    Args:
        match_id (int): The id of the match.
        service (ICardService): The injected service dependency.

    Raises:
        HTTPException: 404 if there are no cards given in the match.

    Returns:
        dict: The requested cards.
    """

    if cards := await service.get_by_match(match_id):
        return cards

    raise HTTPException(status_code=404, detail="Cards not found")


@router.get("/player/{player_api_id}", response_model=Iterable[CardDTO], status_code=200)
@inject
async def get_cards_by_player(
        player_api_id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> Iterable:
    """An endpoint for getting cards given to a player.

    Args:
        player_api_id (int): id of a player.
        service (ICardService): The injected service dependency.

    Raises:
        HTTPException: 404 if player was not given a card.

    Returns:
        dict: The cards the player has been given.
    """

    if cards := await service.get_by_player(player_api_id):
        return cards

    raise HTTPException(status_code=404, detail="Cards not found")


@router.get("/id/{id}", response_model=CardDTO, status_code=200)
@inject
async def get_cards_by_id(
        id: int,
        service: ICardService = Depends(Provide[Container.card_service]),
) -> dict:
    """An endpoint for getting card details by id.

    Args:
        id (int): The id of the card.
        service (ICardService): The injected service dependency.

    Raises:
        HTTPException: 404 if card does not exist.

    Returns:
        dict: The requested card.
    """

    if card := await service.get_by_id(id):
        return card.model_dump()

    raise HTTPException(status_code=404, detail="Card not found")
