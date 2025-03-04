"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.carddb import CardRepository
from src.infrastructure.repositories.countrydb import \
    CountryRepository
from src.infrastructure.repositories.goaldb import GoalRepository
from src.infrastructure.repositories.leaguedb import LeagueRepository
from src.infrastructure.repositories.matchdb import MatchRepository
from src.infrastructure.repositories.oddsdb import OddsRepository
from src.infrastructure.repositories.player_attributesdb import PlayerAttributesRepository
from src.infrastructure.repositories.playerdb import PlayerRepository
from src.infrastructure.repositories.team_attributesdb import TeamAttributesRepository
from src.infrastructure.repositories.teamdb import TeamRepository
from src.infrastructure.services.card import CardService
from src.infrastructure.services.country import CountryService
from src.infrastructure.services.goal import GoalService
from src.infrastructure.services.league import LeagueService
from src.infrastructure.services.match import MatchService
from src.infrastructure.services.odds import OddsService
from src.infrastructure.services.player import PlayerService
from src.infrastructure.services.player_attributes import PlayerAttributesService
from src.infrastructure.services.team import TeamService
from src.infrastructure.services.team_attributes import TeamAttributesService
from src.rabbitmq import OddsRpcClient


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    country_repository = Singleton(CountryRepository)
    league_repository = Singleton(LeagueRepository)
    card_repository = Singleton(CardRepository)
    goal_repository = Singleton(GoalRepository)
    match_repository = Singleton(MatchRepository)
    odds_repository = Singleton(OddsRepository)
    player_repository = Singleton(PlayerRepository)
    player_attributes_repository = Singleton(PlayerAttributesRepository)
    team_repository = Singleton(TeamRepository)
    team_attributes_repository = Singleton(TeamAttributesRepository)
    rpc_client = Singleton(OddsRpcClient)

    country_service = Factory(
        CountryService,
        repository=country_repository,
    )

    league_service = Factory(
        LeagueService,
        repository=league_repository
    )

    card_service = Factory(
        CardService,
        repository=card_repository
    )

    goal_service = Factory(
        GoalService,
        repository=goal_repository
    )

    match_service = Factory(
        MatchService,
        repository=match_repository
    )

    player_service = Factory(
        PlayerService,
        repository=player_repository
    )

    player_attributes_service = Factory(
        PlayerAttributesService,
        repository=player_attributes_repository
    )

    team_service = Factory(
        TeamService,
        repository=team_repository
    )

    team_attributes_service = Factory(
        TeamAttributesService,
        repository=team_attributes_repository
    )

    odds_service = Factory(
        OddsService,
        repository=odds_repository
    )
