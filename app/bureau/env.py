import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS= 'kafka:9092'
KAFKA_TOPIC='shipp'
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()