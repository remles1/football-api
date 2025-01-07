"""Module containing league-related domain models"""

from pydantic import BaseModel, ConfigDict


class LeagueIn(BaseModel):
    """Model representing league's DTO attributes."""
    country_id: int
    name: str


class League(LeagueIn):
    """Model representing league's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
