from fastapi import FastAPI
from routes.buy import buy
#from routes.consumer import consume
import asyncio

app = FastAPI()
app.include_router(buy, prefix='/buy')







#aprender kafka teorico (documentacion,videos,articulos) broker de mensajeria
#elastic search
#asyncio

#proyecto
#pequeña aplicacion distribuida de 2 aplicaciones separadas
#aplicacion de ventas (1er microservicio) 
#API REST crear una venta (una serie de articulos que fueron comprados a traves de un medio de pago) 
#cuando crea la venta emite un evento a kafka (evento venta creada)

# shipping (2do microservicio)
#cada vez que alguien compra algo y se observa en la venta el va a reaccionar al evento que se emitio en kafka
#necesita crear un envio a tal direccion de forma que se le envian los articulos a la persona
#microservicio que consume eventos de kafka

#(todo de forma asincrona) todo en docker y docker-compose
#base de datos de elastic search (ambos microservices)

#algoritmos de balanceo en elastic search

#reverse index elastic search

#para la otra semana es la expectativa de esta semana buen dominio de elastic search y kafka y proyecto inicicado

#   - KAFKA_CFG_ADVERTISED_HOST_NAME=127.0.0.10
#      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
#


#reutilizar el productor en varias request


#ejecutar consumidor como script (sin servidor http)
#elasticsearch para guardar