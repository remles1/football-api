"""Module containing Country-related domain models"""

from pydantic import BaseModel, ConfigDict


class CountryIn(BaseModel):
    """Model representing country's DTO attributes."""
    name: str


class Country(CountryIn):
    """Model representing continent's attributes in the database."""
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
