from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import CatalogModel, EditProduct, CreateProduct
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE ADD PRODUCT IN CATALOG
@router.post(
    "/productcatalog",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def add_product(
    product: CreateProduct,
    db: Session = Depends(get_session),
):
    try:
        new_product = crud.add_product(db, product)
        # Logando dados importantes
        logger.info(
            f"Produto criado com sucesso: {new_product.description} (ID: {new_product.product_id})"
        )
        return new_product
    except Exception as e:
        traceback.print_exc()
        # Logando o erro
        logger.error(f"Erro ao criar produto: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# # Publica os dados do novo produto no RabbitMQ
#     connection = await get_rabbit_connection()
#     async with connection:
#         channel = await connection.channel()
#         await channel.default_exchange.publish(
#             aio_pika.Message(
#             body=json.dumps({
#                 "info_produto": {
#                 product.product_id,
#                 product.code,
#                 product.barcode,
#                 product.description,
#                 product.supplier_name,
#                 product.restockPoint,
#                 product.cost,
#                 product.unit,
#                 product.stockPrice,
#                 product.stockLocation
#                 }
#             }).encode()
#             ),
#             routing_key=QUEUE_NAME
#         )
#     return {"mensagem": "Produto criado com sucesso."}

# ROUTE GET PRODUCT FROM CATALOG
@router.get("/productcatalog/{product_id}", response_model=None)
def get_product(product_id, db: Session = Depends(get_session)):

    product = crud.get_product_by_id(db, product_id)
    if not product:
        logger.warning(f"Produto não encontrado: ID {product_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )

    logger.info(f"Produto acessado: {product.description} (ID: {product.product_id})")
    return product

# ROUTE EDIT PRODUCT FROM CATALOG
@router.put("/productcatalog/{product_id}", response_model=None)
def edit_product(
    product_id: int,
    product: EditProduct,
    db: Session = Depends(get_session),
):
    product_updated = crud.edit_product(db, product_id, product)
    if not product_updated:
        logger.warning(
            f"Tentativa de atualização de produto não encontrado: ID {product_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )

    logger.info(
        f"Produto atualizado com sucesso: {product_updated.description} (ID: {product_updated.product_id})"
    )
    return product_updated

# # Publica os dados do produto editado no RabbitMQ
#     connection = await get_rabbit_connection()
#     async with connection:
#         channel = await connection.channel()
#         await channel.default_exchange.publish(
#             aio_pika.Message(
#             body=json.dumps({
#                 "info_produto": {
#                 product.product_id,
#                 product.code,
#                 product.barcode,
#                 product.description,
#                 product.supplier_name,
#                 product.restockPoint,
#                 product.cost,
#                 product.unit,
#                 product.stockPrice,
#                 product.stockLocation
#                 }
#             }).encode()
#             ),
#             routing_key=QUEUE_NAME
#         )
#     return {"mensagem": "Produto editado com sucesso."}

# ROUTE DELETE PRODUCT FROM CATALOG
@router.delete("/productcatalog/{}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_session),
):
    if not crud.delete_product(db, product_id):
        logger.warning(
            f"Tentativa de deletação de produto não encontrado: ID {product_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )

    logger.info(f"Produto deletado com sucesso: ID {product_id}")
    return {"msg": "Produto deletado com sucesso."}

# # Publica produto deletado no RabbitMQ
#     connection = await get_rabbit_connection()
#     async with connection:
#         channel = await connection.channel()
#         await channel.default_exchange.publish(
#             aio_pika.Message(
#             body=json.dumps({
#                 "info_produto": {
#                 product_id
#                 }
#             }).encode()
#             ),
#             routing_key=QUEUE_NAME
#         )
#     return {"mensagem": "Product deleted"}
# # Encerra a conexão com o banco de dados
#     db.commit()
#     db.close()