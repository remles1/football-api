"""Module containing league repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from sqlalchemy import join, select

from src.core.repositories.ileague import ILeagueRepository
from src.db import league_table, country_table, database
from src.infrastructure.dto.leaguedto import LeagueDTO


class LeagueRepository(ILeagueRepository):
    """A class implementing protocol of league repository."""

    async def get_all_leagues(self) -> Iterable[Any]:
        """The abstract getting all leagues from the data storage.

        Returns:
            Iterable[Any]: Leagues in the data storage.
        """
        query = select(league_table, country_table).select_from(
            join(league_table, country_table, league_table.c.country_id == country_table.c.id)
        )
        leagues = await database.fetch_all(query)
        return [LeagueDTO.from_record(league) for league in leagues]

    async def get_by_country(self, country_id: int) -> Any | None:
        """The abstract getting a league assigned to a Country.

        Args:
            country_id (int): The id of the country.

        Returns:
            Any | None: The league details.
        """
        query = select(league_table, country_table).where(league_table.c.country_id == country_id).select_from(
            join(league_table, country_table,
                 league_table.c.country_id == country_table.c.id
                 )
        )
        league = await database.fetch_one(query)
        return LeagueDTO.from_record(league)

    async def get_by_name(self, name: str) -> Any | None:
        """The abstract getting a league by its name.

        Args:
            name (str): The name of the league.

        Returns:
            Any | None: The league details.
        """
        query = select(league_table, country_table).where(league_table.c.name == name).select_from(
            join(league_table, country_table, league_table.c.country_id == country_table.c.id
                 )
        )
        league = await database.fetch_one(query)
        return LeagueDTO.from_record(league)

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a league by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The league details.
        """
        query = select(league_table, country_table).where(league_table.c.id == id).select_from(
            join(league_table, country_table, league_table.c.country_id == country_table.c.id
                 )
        )
        league = await database.fetch_one(query)
        return LeagueDTO.from_record(league)
