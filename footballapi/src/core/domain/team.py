"""Module containing team-related domain models"""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class TeamIn(BaseModel):
    """Model representing teams DTO attributes."""
    team_api_id: int
    team_fifa_api_id: Optional[int] = None
    team_long_name: str
    team_short_name: str


class Team(TeamIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
