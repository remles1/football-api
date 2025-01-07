"""A module containing DTO models for output Players."""
from typing import Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class PlayerDTO(BaseModel):
    """A model representing DTO for Player data."""
    id: int
    player_api_id: int
    player_name: str
    player_fifa_api_id: int
    birthday: str
    height: int
    weight: int

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
            PlayerDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            player_api_id=record_dict.get("player_api_id"),
            player_name=record_dict.get("player_name"),
            player_fifa_api_id=record_dict.get("player_fifa_api_id"),
            birthday=record_dict.get("birthday"),
            height=record_dict.get("height"),
            weight=record_dict.get("weight"),
        )
