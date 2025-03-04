"""Module containing card repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.domain.card import Card
from src.core.repositories.icard import ICardRepository
from src.db import card_table, database

from src.infrastructure.dto.carddto import CardDTO


class CardRepository(ICardRepository):
    """A class implementing the database country repository."""

    async def get_all_cards(self) -> Iterable[Any]:
        """The abstract getting all cards from the data storage.

        Returns:
            Iterable[Any]: Cards in the data storage.
        """
        query = card_table.select()
        cards = await database.fetch_all(query)
        return [Card(**dict(card)) for card in cards]

    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting cards given in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Cards assigned to the match.
        """
        query = card_table.select().where(card_table.c.match_id == match_id)
        cards = await database.fetch_all(query)

        return [CardDTO.from_record(card) for card in cards]

    async def get_by_player(self, player: int) -> Iterable[Any]:
        """The abstract getting airports assigned to particular continent.

        Args:
            player (int): The player_api_id of the player.

        Returns:
            Iterable[Any]: Every card given to a player.
        """
        query = card_table.select().where(card_table.c.player == player)
        cards = await database.fetch_all(query)

        return [CardDTO.from_record(card) for card in cards]

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a card by provided id.

        Args:
            id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """
        query = card_table.select().where(card_table.c.id == id)
        card = await database.fetch_one(query)

        return CardDTO.from_record(card) if card else None
