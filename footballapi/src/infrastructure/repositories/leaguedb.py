"""Module containing league repository abstractions."""

from typing import Any, Iterable

from sqlalchemy import join, select, func, and_

from src.core.repositories.ileague import ILeagueRepository
from src.db import league_table, country_table, database, match_table, team_table, card_table
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

    async def _get_matches_played_count_in_every_season(self, id: int) -> Any | None:
        """The abstract getting a league statistics by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The requested stats.
        """
        query = select(
            match_table.c.season,
            func.count(match_table.c.id).label("matches_played"),
            func.sum(match_table.c.home_team_goal + match_table.c.away_team_goal).label("total_goals"),
        ).where(match_table.c.league_id == id).group_by(match_table.c.season).order_by(match_table.c.season)

        result = await database.fetch_all(query)
        return result

    async def stats(self, id: int) -> Any | None:
        """The abstract getting a league statistics by provided id.

        Args:
            id (int): The id of the league.

        Returns:
            Any | None: The requested stats.
        """

        total_goals_query = select(
            match_table.c.season,
            func.count(match_table.c.id).label("matches_played"),
            func.sum(match_table.c.home_team_goal + match_table.c.away_team_goal).label("total_goals"),
        ).where(match_table.c.league_id == id).group_by(match_table.c.season).order_by(match_table.c.season)

        total_goals_result = await database.fetch_all(total_goals_query)

        winning_team_home_query = select(
            team_table.c.team_long_name,
            func.count().label("wins")
        ).select_from(
            join(team_table, match_table, team_table.c.team_api_id == match_table.c.home_team_api_id)
        ).where(
            and_(
                match_table.c.home_team_goal > match_table.c.away_team_goal,
                match_table.c.league_id == id
            )
        ).group_by(team_table.c.team_long_name)

        winning_team_away_query = select(
            team_table.c.team_long_name,
            func.count().label("wins")
        ).select_from(
            join(team_table, match_table, team_table.c.team_api_id == match_table.c.away_team_api_id)
        ).where(
            and_(
                match_table.c.away_team_goal > match_table.c.home_team_goal,
                match_table.c.league_id == id
            )
        ).group_by(team_table.c.team_long_name)

        winning_team_results_subquery = winning_team_home_query.union_all(winning_team_away_query).subquery()

        winning_team_query_combined = (select(
            winning_team_results_subquery.c.team_long_name,
            func.sum(winning_team_results_subquery.c.wins).label("total_wins")
        ).group_by(
            winning_team_results_subquery.c.team_long_name
        ).order_by(
            func.sum(winning_team_results_subquery.c.wins).desc()
        )
        )

        winning_team_result = await database.fetch_one(winning_team_query_combined)

        card_counts_query = (select(
            match_table.c.season,
            card_table.c.card_type,
            func.count(card_table.c.card_type).label("total_cards")
        ).where(
            match_table.c.league_id == id
        ).select_from(
            join(match_table, card_table, match_table.c.match_api_id == card_table.c.match_id)
        ).group_by(
            match_table.c.season,
            card_table.c.card_type
        ).order_by(
            match_table.c.season,
            card_table.c.card_type
        ))

        card_counts_result = await database.fetch_all(card_counts_query)

        cards_by_season = {}
        for row in card_counts_result:

            season = row.season
            if season not in cards_by_season:
                cards_by_season[season] = []
            cards_by_season[season].append({
                "card_type": row.card_type,
                "total_cards": row.total_cards
            })

        results_dict = {
            "seasons": [
                {"season": row.season,
                 "matches_played": row.matches_played,
                 "total_goals": row.total_goals,
                 "cards": cards_by_season.get(row.season, [])
                 }
                for row in total_goals_result
            ],
            "most_wins": {
                "name": winning_team_result.team_long_name if winning_team_result else None,
                "wins": winning_team_result.total_wins if winning_team_result else None
            }
        }

        return results_dict
