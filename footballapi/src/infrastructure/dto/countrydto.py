"""A module containing DTO models for output Countries."""
from typing import Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class CountryDTO(BaseModel):
    """A model representing DTO for country data."""
    id: int
    name: str
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
            CountryDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            name=record_dict.get("name")
        )
