from fastapi import FastAPI, Depends
import aio_pika
import asyncio
import json
import os
import logging
from sqlalchemy.orm import Session
from database import get_session, Base, engine
from models import UsuarioModel

# Configuração do logger para registrar eventos e erros
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Configuração do RabbitMQ com credenciais e host definidos nas variáveis de ambiente
RABBITMQ_URL = f"amqp://{os.environ['RABBITMQ_USER']}:{os.environ['RABBITMQ_PASS']}@{os.environ['RABBITMQ_HOST']}/"
QUEUE_NAME = "product.events"

async def process_incoming_message(message: aio_pika.IncomingMessage):
    """
    Processa mensagens recebidas da fila do RabbitMQ.
    - Faz a leitura e o reconhecimento (ack) da mensagem.
    - Decodifica o JSON e extrai os dados do usuário.
    - Insere o usuário no banco de dados.
    """
    message.ack()  # Confirma o recebimento da mensagem
    body = message.body
    logger.info("Received message")

    if body:
        parsed_message = json.loads(body)
        info_produto = parsed_message['info_produto']
        product_id = info_produto['id']

        # Obtém uma sessão do banco de dados
        session: Session = next(get_session())
        stock_update()  

async def stock_update():
    # Verifica se já existe registro de estoque para o produto "product_id"
    stock = db.query(StockModel).filter(StockModel.product_id == product_id).first()
    
    # Se não existir, cria um novo registro de estoque
    if not stock:
        try:
            stock = StockModel(
                stock_id = str,
                product_id = info_produto['product_id'],
                code = info_produto['code'],
                barcode = info_produto['barcode'],
                description = info_produto['description'],
                supplier_name = info_produto['supplier_name'],
                restockPoint = info_produto['restockPoint'],
                cost = info_produto['cost'],
                stockAtualDate = default=func.now(),
                stockQty = 0,
                inventoryDate = default=func.now(),
                inventoryQty = 0,
                totalEntries = 0,
                totalExits = 0,
                unit=info_produto['unit'],
                stockPrice=info_produto['stockPrice'],
                stockLocation=info_produto['stockLocation'],
                last_update = default=func.now(),
                user_id = user_id
            )
            session.add(stock)
            session.commit()
            logger.info(f"Estoque do produto {stock.product_id} criado com sucesso.")
        except Exception as e:
            session.rollback()
            logger.error(f"Erro ao processar mensagem: {str(e)}")
        finally:
            session.close()
        logger.info(f"Message content: {parsed_message}")

    # ou apenas atualiza
    else:    
        try:
            stock.code = info_produto['code'],
            stock.barcode = info_produto['barcode'],
            stock.description = info_produto['description'],
            stock.supplier_name = info_produto['supplier_name'],
            stock.restockPoint = info_produto['restockPoint'],
            stock.cost = info_produto['cost'],
            stock.unit=info_produto['unit'],
            stock.stockPrice=info_produto['stockPrice'],
            stock.stockLocation=info_produto['stockLocation'],
            stock.last_update = default=func.now()
    # commit
            session.commit(stock)
            logger.info(f"Estoque do produto {product_id} atualizado com sucesso.")
        except Exception as e:
            session.rollback()
            logger.error(f"Erro ao processar mensagem: {str(e)}")
        finally:
            session.close()
        logger.info(f"Message content: {parsed_message}")

async def consume(loop):
    """
    Inicializa o consumidor de mensagens do RabbitMQ.
    - Estabelece a conexão com o RabbitMQ.
    - Declara a fila e começa a escutar mensagens.
    - Chama 'process_incoming_message' ao receber uma nova mensagem.
    """
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL, loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(QUEUE_NAME)
        await queue.consume(process_incoming_message, no_ack=False)
        logger.info("Waiting for messages...")
        return connection
    except Exception as e:
        logger.error(f"Erro no consumidor: {e}")
