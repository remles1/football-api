"""Module containing odds repository implementations."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from sqlalchemy import Date, cast

from src.core.repositories.iodds import IOddsRepository
from src.db import match_table, database


class OddsRepository(IOddsRepository):
    """A class representing protocol of odds repository."""

    async def get_previous_matches(self, match_api_id: int) -> Iterable[Any] | None:
        """The abstract getting previous 11 matches
        in a league in the same season. Used for predicting winning odds.

        Args:
            match_api_id (int): match_api_id of the match of which we are predicting odds

        Returns:
            Iterable[Any]: Matches.
        """

        query_current_match = match_table.select().where(match_table.c.match_api_id == match_api_id)
        current_match = await database.fetch_one(query_current_match)

        if not current_match:
            return None

        league_id = current_match.league_id
        season = current_match.season

        query_previous_matches = match_table.select().filter(
            match_table.c.league_id == league_id,
            match_table.c.season == season,
            match_table.c.date < current_match.date
        ).order_by(match_table.c.date.desc()).limit(10)

        result = await database.fetch_all(query_previous_matches)
        result.insert(0, current_match)
        return result
