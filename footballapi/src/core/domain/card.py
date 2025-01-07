"""Module containing Card-related domain models"""
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CardIn(BaseModel):
    """Model representing card's DTO attributes."""
    match_id: int
    elapsed: int
    card_type: str
    player: Optional[int] = None


class Card(CardIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
