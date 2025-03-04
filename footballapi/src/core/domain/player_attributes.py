"""Module containing player_attribute-related domain models"""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class MatchIn(BaseModel):
    """Model representing player_attribute DTO attributes."""
    player_fifa_api_id: int
    player_api_id: int
    date: str
    overall_rating: int
    potential: int
    preferred_foot: str
    attacking_work_rate: str
    defensive_work_rate: str
    crossing: Optional[int] = None
    finishing: Optional[int] = None
    heading_accuracy: Optional[int] = None
    short_passing: Optional[int] = None
    volleys: Optional[int] = None
    dribbling: Optional[int] = None
    curve: Optional[int] = None
    free_kick_accuracy: Optional[int] = None
    long_passing: Optional[int] = None
    ball_control: Optional[int] = None
    acceleration: Optional[int] = None
    sprint_speed: Optional[int] = None
    agility: Optional[int] = None
    reactions: Optional[int] = None
    balance: Optional[int] = None
    shot_power: Optional[int] = None
    jumping: Optional[int] = None
    stamina: Optional[int] = None
    strength: Optional[int] = None
    long_shots: Optional[int] = None
    aggression: Optional[int] = None
    interceptions: Optional[int] = None
    positioning: Optional[int] = None
    vision: Optional[int] = None
    penalties: Optional[int] = None
    marking: Optional[int] = None
    standing_tackle: Optional[int] = None
    sliding_tackle: Optional[int] = None
    gk_diving: Optional[int] = None
    gk_handling: Optional[int] = None
    gk_kicking: Optional[int] = None
    gk_positioning: Optional[int] = None
    gk_reflexes: Optional[int] = None


class Match(MatchIn):
    """Model representing player_attribute attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
