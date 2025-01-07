"""Module containing Goal-related domain models"""
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GoalIn(BaseModel):
    """Model representing Goal's DTO attributes."""

    match_id: int
    scorer: Optional[int] = None
    assister: Optional[int] = None
    elapsed: int
    team: int
    goal_type: str


class Goal(GoalIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
