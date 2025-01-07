"""Module containing card service implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.repositories.icard import ICardRepository

from src.infrastructure.services.icard import ICardService


class CardService(ICardService):
    """A class representing protocol of card service."""

    _repository: ICardRepository

    def __init__(self, repository: ICardRepository):
        """The initializer of the `card service`.

            Args:
                repository (ICardRepository): The reference to the repository.
            """
        self._repository = repository

    async def get_all_cards(self) -> Iterable[Any]:
        """The abstract getting all cards from the data storage.

        Returns:
            Iterable[Any]: Cards in the data storage.
        """
        return await self._repository.get_all_cards()

    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting cards given in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Cards assigned to the match.
        """
        return await self._repository.get_by_match(match_id)

    async def get_by_player(self, player: int) -> Iterable[Any]:
        """The abstract getting cards given to a particular player.

        Args:
            player (int): The player_api_id of the player.

        Returns:
            Iterable[Any]: Every card given to a particular player.
        """
        return await self._repository.get_by_player(player)

    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a card by provided id.

        Args:
            id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """
        return await self._repository.get_by_id(id)
