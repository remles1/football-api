"""A module containing country endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.country import Country
from src.infrastructure.services.icountry import ICountryService

router = APIRouter()


@router.get("/all", response_model=Iterable[Country], status_code=200)
@inject
async def get_all_countries(
        service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:
    """An endpoint for getting all countries.

    Args:
        service (ICountryService): The injected service dependency.

    Returns:
        Iterable: The country attributes collection.
    """

    countries = await service.get_all_countries()

    return countries


@router.get("/name/{name}", response_model=Country, status_code=200)
@inject
async def get_country_by_name(
        name: str,
        service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict:
    """An endpoint for getting country details by id.

    Args:
        name (str): The id of the country.
        service (ICountryService): The injected service dependency.

    Raises:
        HTTPException: 404 if country does not exist.

    Returns:
        dict: The requested country attributes.
    """

    if country := await service.get_by_name(name=name):
        return country.model_dump()

    raise HTTPException(status_code=404, detail="Country not found")


@router.get("/id/{id}", response_model=Country, status_code=200)
@inject
async def get_country_by_id(
        id: int,
        service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict:
    """An endpoint for getting country details by id.

    Args:
        id (int): The id of the country.
        service (ICountryService): The injected service dependency.

    Raises:
        HTTPException: 404 if country does not exist.

    Returns:
        dict: The requested country attributes.
    """

    if country := await service.get_by_id(id=id):
        return country.model_dump()

    raise HTTPException(status_code=404, detail="Country not found")
