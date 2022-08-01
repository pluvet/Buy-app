from aiokafka import AIOKafkaProducer
import os
from random import randint
from env import loop


# env variables

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
kafka_group = 'sell'

producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

