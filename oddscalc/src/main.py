import asyncio
import logging

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from aio_pika import Message, connect
from aio_pika.abc import AbstractIncomingMessage
from aiormq import AMQPConnectionError
from scipy.stats import poisson

from config import config


async def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam,
                                                           'opponent': awayTeam, 'home': 1},
                                                     index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam,
                                                           'opponent': homeTeam, 'home': 0},
                                                     index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)] for team_avg in
                 [home_goals_avg, away_goals_avg]]
    return (np.outer(np.array(team_pred[0]), np.array(team_pred[1])))


async def calc_odds(data: str) -> dict:
    # data = data.decode('utf-8')
    if not data:
        return {}
    df = pd.read_json(data)

    hometeam = df['home_team_api_id'].iloc[0]
    awayteam = df['away_team_api_id'].iloc[0]


    df = df.drop(0)  # drop mecz dla ktorego liczymy szanse
    df = df[["home_team_api_id", "away_team_api_id", "home_team_goal", "away_team_goal"]]
    df = df.rename(columns={'home_team_goal': 'HomeGoals', 'away_team_goal': 'AwayGoals'})

    print(df)

    goal_model_data = pd.concat([df[['home_team_api_id', 'away_team_api_id', 'HomeGoals']].assign(home=1).rename(
        columns={'home_team_api_id': 'team', 'away_team_api_id': 'opponent', 'HomeGoals': 'goals'}),
        df[['away_team_api_id', 'home_team_api_id', 'AwayGoals']].assign(home=0).rename(
            columns={'away_team_api_id': 'team', 'home_team_api_id': 'opponent', 'AwayGoals': 'goals'})])

    poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data,
                            family=sm.families.Poisson()).fit()

    decyzja = await simulate_match(poisson_model, hometeam, awayteam, max_goals=10)
    print(f"{hometeam} win: {np.sum(np.tril(decyzja, -1))}")
    print(f"remis: {np.sum(np.diag(decyzja))}")
    print(f"{awayteam} win: {np.sum(np.triu(decyzja, 1))}")
    print(f"suma: {np.sum(np.tril(decyzja, -1)) + np.sum(np.diag(decyzja)) + np.sum(np.triu(decyzja, 1))}")

    return_dict = {"home_team": float(np.sum(np.tril(decyzja, -1))), "draw": float(np.sum(np.diag(decyzja))),
                   "away_team": float(np.sum(np.triu(decyzja, 1)))}

    return return_dict


async def main(retries: int = 5, delay: int = 5) -> None:
    conn_successful = False
    connection = None
    for attempt in range(retries):
        try:
            connection = await connect(
                f"amqp://{config.RABBITMQ_DEFAULT_USER}:{config.RABBITMQ_DEFAULT_PASS}@{config.RABBITMQ_HOST}:{config.RABBITMQ_PORT}/")
            conn_successful = True
            break
        except AMQPConnectionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    if not conn_successful:
        raise ConnectionError("Could not connect to RabbitMQ after several retries")

    channel = await connection.channel()
    exchange = channel.default_exchange

    queue = await channel.declare_queue("rpc_queue")
    print(" [x] Awaiting RPC requests")
    async with queue.iterator() as qiterator:
        message: AbstractIncomingMessage
        async for message in qiterator:
            try:
                async with message.process(requeue=False):
                    assert message.reply_to is not None
                    data = message.body.decode()

                    response = str(await calc_odds(data)).encode()
                    await exchange.publish(
                        Message(
                            body=response,
                            correlation_id=message.correlation_id,
                        ), routing_key=message.reply_to, )
                    print("Request complete")
            except Exception:
                logging.exception("Processing error for message %r", message)


if __name__ == "__main__":
    # time.sleep(10)
    asyncio.run(main())
