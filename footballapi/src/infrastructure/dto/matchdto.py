"""A module containing DTO models for output Matches."""
import asyncio
from typing import Optional, Iterable, Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict

from src.core.repositories.icard import ICardRepository
from src.core.repositories.igoal import IGoalRepository
from src.infrastructure.dto.carddto import CardDTO
from src.infrastructure.dto.goaldto import GoalDTO


class MatchDTO(BaseModel):
    """A model representing DTO for match data."""
    id: int
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
    goals: Optional[Iterable[GoalDTO]] = None
    cards: Optional[Iterable[CardDTO]] = None
    # B365H: Optional[float] = None
    # B365D: Optional[float] = None
    # B365A: Optional[float] = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    async def from_record(cls, record: Record, card_repo_interface: ICardRepository, goal_repo_interface: IGoalRepository) -> Self | None:
        """A method for preparing DTO instance based on DB records.

        Args:
            record (Record): The DB record.
            card_repo_interface (ICardRepository): Card repository interface used to return cards awarded in a match.
            goal_repo_interface (IGoalRepository): Goal repository interface used to return goals.

        Returns:
            MatchDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            country_id=record_dict.get("country_id"),
            league_id=record_dict.get("league_id"),
            season=record_dict.get("season"),
            stage=record_dict.get("stage"),
            date=record_dict.get("date"),
            match_api_id=record_dict.get("match_api_id"),
            home_team_api_id=record_dict.get("home_team_api_id"),
            away_team_api_id=record_dict.get("away_team_api_id"),
            home_team_goal=record_dict.get("home_team_goal"),
            away_team_goal=record_dict.get("away_team_goal"),
            home_player_1=record_dict.get("home_player_1"),
            home_player_2=record_dict.get("home_player_2"),
            home_player_3=record_dict.get("home_player_3"),
            home_player_4=record_dict.get("home_player_4"),
            home_player_5=record_dict.get("home_player_5"),
            home_player_6=record_dict.get("home_player_6"),
            home_player_7=record_dict.get("home_player_7"),
            home_player_8=record_dict.get("home_player_8"),
            home_player_9=record_dict.get("home_player_9"),
            home_player_10=record_dict.get("home_player_10"),
            home_player_11=record_dict.get("home_player_11"),
            away_player_1=record_dict.get("away_player_1"),
            away_player_2=record_dict.get("away_player_2"),
            away_player_3=record_dict.get("away_player_3"),
            away_player_4=record_dict.get("away_player_4"),
            away_player_5=record_dict.get("away_player_5"),
            away_player_6=record_dict.get("away_player_6"),
            away_player_7=record_dict.get("away_player_7"),
            away_player_8=record_dict.get("away_player_8"),
            away_player_9=record_dict.get("away_player_9"),
            away_player_10=record_dict.get("away_player_10"),
            away_player_11=record_dict.get("away_player_11"),
            goals=await goal_repo_interface.get_by_match(record_dict.get("match_api_id")),
            cards=await card_repo_interface.get_by_match(record_dict.get("match_api_id")),


        )
