import aio_pika
import json
import os
from sqlalchemy.orm import Session
from database import get_session, Base, engine
from models import CatalogModel
import logging

# # Configuração do logger para registrar eventos da aplicação
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # Configuração do RabbitMQ com credenciais e host definidos nas variáveis de ambiente
# RABBITMQ_URL = f"amqp://{os.environ['RABBITMQ_USER']}:{os.environ['RABBITMQ_PASS']}@{os.environ['RABBITMQ_HOST']}/"
# QUEUE_NAME = "product.events"

# async def get_rabbit_connection():

    # """
    # Estabelece e retorna uma conexão assíncrona com o RabbitMQ.
    # Essa conexão será usada para enviar mensagens para a fila.
    # """
    # return await aio_pika.connect_robust(RABBITMQ_URL)

# @app.post("/send")
# async def send_message(message: str):
    # """
    # Envia uma mensagem para a fila do RabbitMQ.
    # - Cria uma conexão com o RabbitMQ.
    # - Abre um canal de comunicação.
    # - Publica a mensagem na fila definida.
    # """
    # connection = await get_rabbit_connection()
    # async with connection:
    #     channel = await connection.channel()
    #     await channel.default_exchange.publish(
    #         aio_pika.Message(body=json.dumps({"message": message}).encode()),
    #         routing_key=QUEUE_NAME
    #     )
    # return {"status": "Message sent"}