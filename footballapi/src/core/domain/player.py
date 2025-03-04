"""Module containing player-related domain models"""

from pydantic import BaseModel, ConfigDict


class PlayerIn(BaseModel):
    """Model representing players DTO attributes."""
    player_api_id: int
    player_name: str
    player_fifa_api_id: int
    birthday: str
    height: int
    weight: int


class Player(PlayerIn):
    """Model representing players attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
