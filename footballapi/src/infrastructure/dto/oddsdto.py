"""A module containing DTO models for odds."""
from typing import Self

from pydantic import BaseModel, ConfigDict


class OddsDTO(BaseModel):
    """A model representing DTO for odds data."""
    home_team: float
    draw: float
    away_team: float
    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_dict(cls, json: dict) -> Self | None:
        """A method for preparing OddsDTO instance based on dictionary.

        Args:
            json (dict): The predicted odds.

        Returns:
            OddsDTO: The final DTO instance.
        """

        return cls(
            home_team=json.get("home_team"),
            draw=json.get("draw"),
            away_team=json.get("away_team")
        )
