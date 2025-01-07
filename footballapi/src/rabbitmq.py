import asyncio
import json
import uuid
from typing import MutableMapping

from aio_pika import Message, connect
from aio_pika.abc import (
    AbstractChannel, AbstractConnection, AbstractIncomingMessage, AbstractQueue,
)
from aiormq import AMQPConnectionError

from src.config import config


class OddsRpcClient:
    connection: AbstractConnection
    channel: AbstractChannel
    callback_queue: AbstractQueue

    def __init__(self) -> None:
        self.futures: MutableMapping[str, asyncio.Future] = {}

    async def connect(self, retries: int = 5, delay: int = 5) -> "OddsRpcClient":
        conn_successful = False
        for attempt in range(retries):
            try:
                self.connection = await connect(f"amqp://{config.RABBITMQ_DEFAULT_USER}:{config.RABBITMQ_DEFAULT_PASS}@{config.RABBITMQ_HOST}:{config.RABBITMQ_PORT}/")
                conn_successful = True
                break
            except AMQPConnectionError as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                await asyncio.sleep(delay)

        if not conn_successful:
            raise ConnectionError("Could not connect to RabbitMQ after several retries")

        self.channel = await self.connection.channel()
        self.callback_queue = await self.channel.declare_queue(exclusive=True)
        await self.callback_queue.consume(self.on_response, no_ack=True)
        return self

    async def on_response(self, message: AbstractIncomingMessage) -> None:
        if message.correlation_id is None:
            print(f"Bad message {message!r}")
            return

        future: asyncio.Future = self.futures.pop(message.correlation_id)
        future.set_result(message.body)

    async def call(self, data: str) -> dict:
        correlation_id = str(uuid.uuid4())
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        self.futures[correlation_id] = future
        await self.channel.default_exchange.publish(
            Message(
                str(data).encode(),
                content_type="text/plain",
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name,
            ),
            routing_key="rpc_queue",
        )
        result = await future
        result = result.decode()
        result = result.replace("\'", "\"")
        result = json.loads(result)
        #print(result.decode())
        return result
        #return str(await future)
