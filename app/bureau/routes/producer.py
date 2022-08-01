from datetime import datetime
from aiokafka import AIOKafkaProducer
import asyncio
import json
import os
from random import randint
from env import loop
from fastapi.encoders import jsonable_encoder
from config.kafka import producer
# env variables
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

async def send_one(shipp):

    timestamp = datetime.now()
    shipp = {
        "key": "envio",
        "timestamp": timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
        "headers": "hola",
        "address": shipp.address
    }
    shipp = json_serializer(shipp)
    
    prod = producer
    await prod.start()
    try:
        print('Sendding message with value: ')
        await prod.send_and_wait(topic=KAFKA_TOPIC, value=shipp)

        print("sent")
    finally:
        await prod.stop()
  
    #producer = AIOKafkaProducer(KAFKA_BOOTSTRAP_SERVERS)
    # Get cluster layout and initial topic/partition leadership information
    
    print(KAFKA_TOPIC)
    

#asyncio.run(send_one())
