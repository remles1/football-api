"""Module containing team_attributes-related domain models"""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class TeamIn(BaseModel):
    """Model representing team_attributes's DTO attributes."""
    team_fifa_api_id: int
    team_api_id: int
    date: str
    buildUpPlaySpeed: int
    buildUpPlaySpeedClass: str
    buildUpPlayDribbling: Optional[int] = None
    buildUpPlayDribblingClass: str
    buildUpPlayPassing: int
    buildUpPlayPassingClass: str
    buildUpPlayPositioningClass: str
    chanceCreationPassing: int
    chanceCreationPassingClass: str
    chanceCreationCrossing: int
    chanceCreationCrossingClass: str
    chanceCreationShooting: int
    chanceCreationShootingClass: str
    chanceCreationPositioningClass: str
    defencePressure: int
    defencePressureClass: str
    defenceAggression: int
    defenceAggressionClass: str
    defenceTeamWidth: int
    defenceTeamWidthClass: str
    defenceDefenderLineClass: str


class Team(TeamIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
