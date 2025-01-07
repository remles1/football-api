"""A module containing DTO model for output Cards."""
from typing import Optional, Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class CardDTO(BaseModel):
    """A model representing DTO for country data."""
    id: int
    match_id: int
    elapsed: int
    card_type: str
    player: Optional[int] = None

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
            CardDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            match_id=record_dict.get("match_id"),
            elapsed=record_dict.get("elapsed"),
            card_type=record_dict.get("card_type"),
            player=record_dict.get("player")
        )
