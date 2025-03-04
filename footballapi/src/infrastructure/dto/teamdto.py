"""A module containing DTO models for output Teams."""

from typing import Optional, Self
from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class TeamDTO(BaseModel):
    """A model representing DTO for Team data."""
    id: int
    team_api_id: int
    team_fifa_api_id: Optional[int] = None
    team_long_name: str
    team_short_name: str

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
            TeamDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            team_api_id=record_dict.get("team_api_id"),
            team_fifa_api_id=record_dict.get("team_fifa_api_id"),
            team_long_name=record_dict.get("team_long_name"),
            team_short_name=record_dict.get("team_short_name")
        )
