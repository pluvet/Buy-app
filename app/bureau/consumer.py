import asyncio
from routes.producer import json_serializer
from env import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
from elasticsearch import AsyncElasticsearch, NotFoundError

es = AsyncElasticsearch(hosts=["http://elasticsearch:9200"])

async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, 
                                group_id=KAFKA_CONSUMER_GROUP,
                                enable_auto_commit=True,       
                                auto_commit_interval_ms=1000,  
                                auto_offset_reset="earliest")
    await consumer.start()
    try:
        async for msg in consumer:
            
            print(msg.value)
            shippment = msg.value
            if(await es.indices.exists(index="buy")):           
                await es.index(index="buy", body= shippment)
    finally:
        await consumer.stop()
    print ("finish")

asyncio.run(consume())