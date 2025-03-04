"""A module containing DTO models for output Team Attributes."""
from typing import Optional, Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class TeamAttributesDTO(BaseModel):
    """A model representing DTO for Team Attributes data."""
    id: int
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
            TeamAttributesDTO: The final DTO instance.
        """
        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            team_fifa_api_id=record_dict.get("team_fifa_api_id"),
            team_api_id=record_dict.get("team_api_id"),
            date=record_dict.get("date"),
            buildUpPlaySpeed=record_dict.get("buildUpPlaySpeed"),
            buildUpPlaySpeedClass=record_dict.get("buildUpPlaySpeedClass"),
            buildUpPlayDribbling=record_dict.get("buildUpPlayDribbling"),
            buildUpPlayDribblingClass=record_dict.get("buildUpPlayDribblingClass"),
            buildUpPlayPassing=record_dict.get("buildUpPlayPassing"),
            buildUpPlayPassingClass=record_dict.get("buildUpPlayPassingClass"),
            buildUpPlayPositioningClass=record_dict.get("buildUpPlayPositioningClass"),
            chanceCreationPassing=record_dict.get("chanceCreationPassing"),
            chanceCreationPassingClass=record_dict.get("chanceCreationPassingClass"),
            chanceCreationCrossing=record_dict.get("chanceCreationCrossing"),
            chanceCreationCrossingClass=record_dict.get("chanceCreationCrossingClass"),
            chanceCreationShooting=record_dict.get("chanceCreationShooting"),
            chanceCreationShootingClass=record_dict.get("chanceCreationShootingClass"),
            chanceCreationPositioningClass=record_dict.get("chanceCreationPositioningClass"),
            defencePressure=record_dict.get("defencePressure"),
            defencePressureClass=record_dict.get("defencePressureClass"),
            defenceAggression=record_dict.get("defenceAggression"),
            defenceAggressionClass=record_dict.get("defenceAggressionClass"),
            defenceTeamWidth=record_dict.get("defenceTeamWidth"),
            defenceTeamWidthClass=record_dict.get("defenceTeamWidthClass"),
            defenceDefenderLineClass=record_dict.get("defenceDefenderLineClass")

        )
