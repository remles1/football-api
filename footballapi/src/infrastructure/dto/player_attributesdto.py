"""A module containing DTO models for output Player Attributes."""
from typing import Optional, Self

from asyncpg import Record
from pydantic import BaseModel, ConfigDict


class PlayerAttributesDTO(BaseModel):
    """A model representing DTO for Player Attributes data."""
    id: int
    player_fifa_api_id: int
    player_api_id: int
    date: str
    overall_rating: int
    potential: int
    preferred_foot: str
    attacking_work_rate: str
    defensive_work_rate: str
    crossing: Optional[int] = None
    finishing: Optional[int] = None
    heading_accuracy: Optional[int] = None
    short_passing: Optional[int] = None
    volleys: Optional[int] = None
    dribbling: Optional[int] = None
    curve: Optional[int] = None
    free_kick_accuracy: Optional[int] = None
    long_passing: Optional[int] = None
    ball_control: Optional[int] = None
    acceleration: Optional[int] = None
    sprint_speed: Optional[int] = None
    agility: Optional[int] = None
    reactions: Optional[int] = None
    balance: Optional[int] = None
    shot_power: Optional[int] = None
    jumping: Optional[int] = None
    stamina: Optional[int] = None
    strength: Optional[int] = None
    long_shots: Optional[int] = None
    aggression: Optional[int] = None
    interceptions: Optional[int] = None
    positioning: Optional[int] = None
    vision: Optional[int] = None
    penalties: Optional[int] = None
    marking: Optional[int] = None
    standing_tackle: Optional[int] = None
    sliding_tackle: Optional[int] = None
    gk_diving: Optional[int] = None
    gk_handling: Optional[int] = None
    gk_kicking: Optional[int] = None
    gk_positioning: Optional[int] = None
    gk_reflexes: Optional[int] = None

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
            PlayerAttributesDTO: The final DTO instance.
        """

        if record is None:
            return None
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            player_fifa_api_id=record_dict.get("player_fifa_api_id"),
            player_api_id=record_dict.get("player_api_id"),
            date=record_dict.get("date"),
            overall_rating=record_dict.get("overall_rating"),
            potential=record_dict.get("potential"),
            preferred_foot=record_dict.get("preferred_foot"),
            attacking_work_rate=record_dict.get("attacking_work_rate"),
            defensive_work_rate=record_dict.get("defensive_work_rate"),
            crossing=record_dict.get("crossing"),
            finishing=record_dict.get("finishing"),
            heading_accuracy=record_dict.get("heading_accuracy"),
            short_passing=record_dict.get("short_passing"),
            volleys=record_dict.get("volleys"),
            dribbling=record_dict.get("dribbling"),
            curve=record_dict.get("curve"),
            free_kick_accuracy=record_dict.get("free_kick_accuracy"),
            long_passing=record_dict.get("long_passing"),
            ball_control=record_dict.get("ball_control"),
            acceleration=record_dict.get("acceleration"),
            sprint_speed=record_dict.get("sprint_speed"),
            agility=record_dict.get("agility"),
            reactions=record_dict.get("reactions"),
            balance=record_dict.get("balance"),
            shot_power=record_dict.get("shot_power"),
            jumping=record_dict.get("jumping"),
            stamina=record_dict.get("stamina"),
            strength=record_dict.get("strength"),
            long_shots=record_dict.get("long_shots"),
            aggression=record_dict.get("aggression"),
            interceptions=record_dict.get("interceptions"),
            positioning=record_dict.get("positioning"),
            vision=record_dict.get("vision"),
            penalties=record_dict.get("penalties"),
            marking=record_dict.get("marking"),
            standing_tackle=record_dict.get("standing_tackle"),
            sliding_tackle=record_dict.get("sliding_tackle"),
            gk_diving=record_dict.get("gk_diving"),
            gk_handling=record_dict.get("gk_handling"),
            gk_kicking=record_dict.get("gk_kicking"),
            gk_positioning=record_dict.get("gk_positioning"),
            gk_reflexes=record_dict.get("gk_reflexes")
        )
