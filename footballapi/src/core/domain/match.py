"""Module containing match-related domain models"""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class MatchIn(BaseModel):
    """Model representing matches DTO attributes."""
    country_id: int
    league_id: int
    season: str
    stage: int
    date: str
    match_api_id: int
    home_team_api_id: int
    away_team_api_id: int
    home_team_goal: int
    away_team_goal: int
    home_player_1: Optional[int] = None
    home_player_2: Optional[int] = None
    home_player_3: Optional[int] = None
    home_player_4: Optional[int] = None
    home_player_5: Optional[int] = None
    home_player_6: Optional[int] = None
    home_player_7: Optional[int] = None
    home_player_8: Optional[int] = None
    home_player_9: Optional[int] = None
    home_player_10: Optional[int] = None
    home_player_11: Optional[int] = None
    away_player_1: Optional[int] = None
    away_player_2: Optional[int] = None
    away_player_3: Optional[int] = None
    away_player_4: Optional[int] = None
    away_player_5: Optional[int] = None
    away_player_6: Optional[int] = None
    away_player_7: Optional[int] = None
    away_player_8: Optional[int] = None
    away_player_9: Optional[int] = None
    away_player_10: Optional[int] = None
    away_player_11: Optional[int] = None
    B365H: Optional[float] = None
    B365D: Optional[float] = None
    B365A: Optional[float] = None


class Match(MatchIn):
    """Model representing matches attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
