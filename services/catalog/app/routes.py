from fastapi import APIRouter, HTTPException
import aio_pika
import json
import os
from sqlalchemy.orm import Session
from models import CatalogModel
from database import SessionLocal
from producers import get_rabbit_connection
router = APIRouter()

@router.post("/productcatalog/")
def add_product(product: CatalogModel):
    db: Session = SessionLocal()
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return product
# Publica os dados do novo produto no RabbitMQ
    connection = await get_rabbit_connection()
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(
            body=json.dumps({
                "info_produto": {
                product.product_id,
                product.code,
                product.barcode,
                product.description,
                product.supplier_name,
                product.restockPoint,
                product.cost,
                product.unit,
                product.stockPrice,
                product.stockLocation
                }
            }).encode()
            ),
            routing_key=QUEUE_NAME
        )
    return {"mensagem": "Produto criado com sucesso."}

@router.put("/productcatalog/{product_id}")
def edit_product(product_id: int, product: Catalog):
    db: Session = SessionLocal()
    db_product = db.query(Catalog).filter(Catalog.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Update customer fields here
    db.commit()
    db.close()
    return db_product
# Publica os dados do produto editado no RabbitMQ
    connection = await get_rabbit_connection()
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(
            body=json.dumps({
                "info_produto": {
                product.product_id,
                product.code,
                product.barcode,
                product.description,
                product.supplier_name,
                product.restockPoint,
                product.cost,
                product.unit,
                product.stockPrice,
                product.stockLocation
                }
            }).encode()
            ),
            routing_key=QUEUE_NAME
        )
    return {"mensagem": "Produto editado com sucesso."}

@router.delete("/productcatalog/{product_id}")
def delete_product(product_id: int):
    db: Session = SessionLocal()
    db_product = db.query(Catalog).filter(Catalog.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
# Publica produto deletado no RabbitMQ
    connection = await get_rabbit_connection()
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(
            body=json.dumps({
                "info_produto": {
                product_id}).encode()
            ),
            routing_key=QUEUE_NAME
        )
    return {"mensagem": "Product deleted"}
# Encerra a conexão com o banco de dados
    db.commit()
    db.close()