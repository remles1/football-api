"""A module containing DTO models for output Leagues."""
from typing import Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict

from src.infrastructure.dto.countrydto import CountryDTO


class LeagueDTO(BaseModel):
    """A model representing DTO for league data."""
    id: int
    country: CountryDTO
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
            LeagueDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            country=CountryDTO(
                id=record_dict.get("id_1"),
                name=record_dict.get("name_1")
            ),
            name=record_dict.get("name"),
        )
