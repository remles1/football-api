"""A module containing DTO models for output Goals."""
from typing import Optional, Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict

from src.infrastructure.dto.playerdto import PlayerDTO


class GoalDTO(BaseModel):
    """A model representing DTO for goal data."""
    id: int
    match_id: int
    scorer: Optional[PlayerDTO] = None
    assister: Optional[PlayerDTO] = None
    elapsed: int
    team: int
    goal_type: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> Self | None:
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            GoalDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            match_id=record_dict.get("match_id"),
            scorer=PlayerDTO(
                id=record_dict.get("id_1"),
                player_api_id=record_dict.get("player_api_id"),
                player_name=record_dict.get("player_name"),
                player_fifa_api_id=record_dict.get("player_fifa_api_id"),
                birthday=record_dict.get("birthday"),
                height=record_dict.get("height"),
                weight=record_dict.get("weight"),
            ),
            assister=(
                PlayerDTO(
                    id=record_dict.get("id_2"),
                    player_api_id=record_dict.get("player_api_id_1"),
                    player_name=record_dict.get("player_name_1"),
                    player_fifa_api_id=record_dict.get("player_fifa_api_id_1"),
                    birthday=record_dict.get("birthday_1"),
                    height=record_dict.get("height_1"),
                    weight=record_dict.get("weight_1"),
                ) if record_dict.get("id_2") is not None else None
            ),
            elapsed=record_dict.get("elapsed"),
            team=record_dict.get("team"),
            goal_type=record_dict.get("goal_type")
        )
