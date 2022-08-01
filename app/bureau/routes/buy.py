import ast
import json
import os

from fastapi import APIRouter
import asyncio
from httpx import AsyncClient
from config.db import conn
from models.buy import Buy
from schemas.buy import serializeDict, serializeList
from routes.producer import json_serializer, send_one
from elasticsearch import AsyncElasticsearch, NotFoundError
from env import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

buy = APIRouter()

es = AsyncElasticsearch(hosts=["http://elasticsearch:9200"])


@buy.get('/')
async def find_all():
  data = 0

  return data



@buy.post('/')
async def create(buy: Buy):
  """this function will create the shippment message in kafka and after that save the buy with elasticsearch"""


  await send_one(buy)

  if(await es.indices.exists(index="buy")):
    body = json_serializer(dict(buy))
    await es.index(index="buy", body= body)
    


  return buy








