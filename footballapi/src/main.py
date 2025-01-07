"""Main module of the app"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from src.api.routers.country import router as country_router
from src.api.routers.league import router as league_router
from src.api.routers.card import router as card_router
from src.api.routers.goal import router as goal_router
from src.api.routers.match import router as match_router
from src.api.routers.player import router as player_router
from src.api.routers.player_attributes import router as player_attributes_router
from src.api.routers.team import router as team_router
from src.api.routers.odds import router as odds_router
from src.api.routers.team_attributes import router as team_attributes_router
from src.container import Container
from src.db import database, init_db
from src.rabbitmq import OddsRpcClient

container = Container()
container.wire(modules=[
    "src.api.routers.country",
    "src.api.routers.league",
    "src.api.routers.card",
    "src.api.routers.goal",
    "src.api.routers.match",
    "src.api.routers.player",
    "src.api.routers.player_attributes",
    "src.api.routers.team",
    "src.api.routers.team_attributes",
    "src.api.routers.odds"
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    await Container.rpc_client().connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(country_router, prefix="/country")
app.include_router(league_router, prefix="/league")
app.include_router(card_router, prefix="/card")
app.include_router(goal_router, prefix="/goal")
app.include_router(match_router, prefix="/match")
app.include_router(player_router, prefix="/player")
app.include_router(player_attributes_router, prefix="/player_attr")
app.include_router(team_router, prefix="/team")
app.include_router(team_attributes_router, prefix="/team_attr")
app.include_router(odds_router, prefix="/odds")


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:
    """A function handling http exceptions for logging purposes.

    Args:
        request (Request): The incoming HTTP request.
        exception (HTTPException): A related exception.

    Returns:
        Response: The HTTP response.
    """
    return await http_exception_handler(request, exception)
