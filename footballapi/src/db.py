"""A module providing database access."""

"""
SELECT
    p.player_name,
    COUNT(DISTINCT g.id) AS total_goals,
    COUNT(DISTINCT CASE WHEN c.card_type = 'y' THEN c.id END) AS yellow_cards,
    COUNT(DISTINCT CASE WHEN c.card_type = 'y2' THEN c.id END) AS yellow_red_cards,
    COUNT(DISTINCT CASE WHEN c.card_type = 'r' THEN c.id END) AS red_cards
FROM
    "Player" p
LEFT JOIN
    "Goal" g ON p.player_api_id = g.scorer
LEFT JOIN
    "Card" c ON p.player_api_id = c.player
WHERE
    p.player_api_id = 93447
GROUP BY
    p.player_name
ORDER BY
    p.player_name;

"""


import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (  # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from src.config import config

metadata = sqlalchemy.MetaData()

card_table = sqlalchemy.Table(
    "Card",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("match_id", sqlalchemy.Integer),
    sqlalchemy.Column("elapsed", sqlalchemy.Integer),
    sqlalchemy.Column("card_type", sqlalchemy.String),
    sqlalchemy.Column("player", sqlalchemy.Integer)
)

country_table = sqlalchemy.Table(
    "Country",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

goal_table = sqlalchemy.Table(
    "Goal",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("match_id", sqlalchemy.Integer),
    sqlalchemy.Column("scorer", sqlalchemy.Integer),
    sqlalchemy.Column("assister", sqlalchemy.Integer),
    sqlalchemy.Column("elapsed", sqlalchemy.Integer),
    sqlalchemy.Column("team", sqlalchemy.Integer),
    sqlalchemy.Column("goal_type", sqlalchemy.String)
)

league_table = sqlalchemy.Table(
    "League",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("country_id", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String)
)

match_table = sqlalchemy.Table(
    "Match",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("country_id", sqlalchemy.Integer),
    sqlalchemy.Column("league_id", sqlalchemy.Integer),
    sqlalchemy.Column("season", sqlalchemy.String),
    sqlalchemy.Column("stage", sqlalchemy.Integer),
    sqlalchemy.Column("date", sqlalchemy.Integer),
    sqlalchemy.Column("match_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("home_team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("away_team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("home_team_goal", sqlalchemy.Integer),
    sqlalchemy.Column("away_team_goal", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_1", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_2", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_3", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_4", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_5", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_6", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_7", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_8", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_9", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_10", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_11", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_1", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_2", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_3", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_4", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_5", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_6", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_7", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_8", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_9", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_10", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_11", sqlalchemy.Integer),
)

player_table = sqlalchemy.Table(
    "Player",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("player_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("player_name", sqlalchemy.String),
    sqlalchemy.Column("player_fifa_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("birthday", sqlalchemy.String),
    sqlalchemy.Column("height", sqlalchemy.Integer),
    sqlalchemy.Column("weight", sqlalchemy.Integer)
)

player_attributes_table = sqlalchemy.Table(
    'Player_Attributes', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('player_fifa_api_id', sqlalchemy.Integer),
    sqlalchemy.Column('player_api_id', sqlalchemy.Integer),
    sqlalchemy.Column('date', sqlalchemy.String),
    sqlalchemy.Column('overall_rating', sqlalchemy.Integer),
    sqlalchemy.Column('potential', sqlalchemy.Integer),
    sqlalchemy.Column('preferred_foot', sqlalchemy.String),
    sqlalchemy.Column('attacking_work_rate', sqlalchemy.String),
    sqlalchemy.Column('defensive_work_rate', sqlalchemy.String),
    sqlalchemy.Column('crossing', sqlalchemy.Integer),
    sqlalchemy.Column('finishing', sqlalchemy.Integer),
    sqlalchemy.Column('heading_accuracy', sqlalchemy.Integer),
    sqlalchemy.Column('short_passing', sqlalchemy.Integer),
    sqlalchemy.Column('volleys', sqlalchemy.Integer),
    sqlalchemy.Column('dribbling', sqlalchemy.Integer),
    sqlalchemy.Column('curve', sqlalchemy.Integer),
    sqlalchemy.Column('free_kick_accuracy', sqlalchemy.Integer),
    sqlalchemy.Column('long_passing', sqlalchemy.Integer),
    sqlalchemy.Column('ball_control', sqlalchemy.Integer),
    sqlalchemy.Column('acceleration', sqlalchemy.Integer),
    sqlalchemy.Column('sprint_speed', sqlalchemy.Integer),
    sqlalchemy.Column('agility', sqlalchemy.Integer),
    sqlalchemy.Column('reactions', sqlalchemy.Integer),
    sqlalchemy.Column('balance', sqlalchemy.Integer),
    sqlalchemy.Column('shot_power', sqlalchemy.Integer),
    sqlalchemy.Column('jumping', sqlalchemy.Integer),
    sqlalchemy.Column('stamina', sqlalchemy.Integer),
    sqlalchemy.Column('strength', sqlalchemy.Integer),
    sqlalchemy.Column('long_shots', sqlalchemy.Integer),
    sqlalchemy.Column('aggression', sqlalchemy.Integer),
    sqlalchemy.Column('interceptions', sqlalchemy.Integer),
    sqlalchemy.Column('positioning', sqlalchemy.Integer),
    sqlalchemy.Column('vision', sqlalchemy.Integer),
    sqlalchemy.Column('penalties', sqlalchemy.Integer),
    sqlalchemy.Column('marking', sqlalchemy.Integer),
    sqlalchemy.Column('standing_tackle', sqlalchemy.Integer),
    sqlalchemy.Column('sliding_tackle', sqlalchemy.Integer),
    sqlalchemy.Column('gk_diving', sqlalchemy.Integer),
    sqlalchemy.Column('gk_handling', sqlalchemy.Integer),
    sqlalchemy.Column('gk_kicking', sqlalchemy.Integer),
    sqlalchemy.Column('gk_positioning', sqlalchemy.Integer),
    sqlalchemy.Column('gk_reflexes', sqlalchemy.Integer)
)

team_table = sqlalchemy.Table(
    "Team",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("team_fifa_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("team_long_name", sqlalchemy.String),
    sqlalchemy.Column("team_short_name", sqlalchemy.String)
)

team_attributes_table = sqlalchemy.Table(
    'Team_Attributes', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('team_fifa_api_id', sqlalchemy.Integer),
    sqlalchemy.Column('team_api_id', sqlalchemy.Integer),
    sqlalchemy.Column('date', sqlalchemy.String),
    sqlalchemy.Column('buildUpPlaySpeed', sqlalchemy.Integer),
    sqlalchemy.Column('buildUpPlaySpeedClass', sqlalchemy.String),
    sqlalchemy.Column('buildUpPlayDribbling', sqlalchemy.Integer),
    sqlalchemy.Column('buildUpPlayDribblingClass', sqlalchemy.String),
    sqlalchemy.Column('buildUpPlayPassing', sqlalchemy.Integer),
    sqlalchemy.Column('buildUpPlayPassingClass', sqlalchemy.String),
    sqlalchemy.Column('buildUpPlayPositioningClass', sqlalchemy.String),
    sqlalchemy.Column('chanceCreationPassing', sqlalchemy.Integer),
    sqlalchemy.Column('chanceCreationPassingClass', sqlalchemy.String),
    sqlalchemy.Column('chanceCreationCrossing', sqlalchemy.Integer),
    sqlalchemy.Column('chanceCreationCrossingClass', sqlalchemy.String),
    sqlalchemy.Column('chanceCreationShooting', sqlalchemy.Integer),
    sqlalchemy.Column('chanceCreationShootingClass', sqlalchemy.String),
    sqlalchemy.Column('chanceCreationPositioningClass', sqlalchemy.String),
    sqlalchemy.Column('defencePressure', sqlalchemy.Integer),
    sqlalchemy.Column('defencePressureClass', sqlalchemy.String),
    sqlalchemy.Column('defenceAggression', sqlalchemy.Integer),
    sqlalchemy.Column('defenceAggressionClass', sqlalchemy.String),
    sqlalchemy.Column('defenceTeamWidth', sqlalchemy.Integer),
    sqlalchemy.Column('defenceTeamWidthClass', sqlalchemy.String),
    sqlalchemy.Column('defenceDefenderLineClass', sqlalchemy.String)
)

db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.execute(sqlalchemy.text("SELECT 1"))
            return
        except (
                OperationalError,
                DatabaseError,
                CannotConnectNowError,
                ConnectionRefusedError,
                ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")
