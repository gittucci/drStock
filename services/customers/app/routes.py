from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import CustomersModel, EditCustomer, CreateCustomer
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE ADD CUSTOMER IN CUSTOMERS
@router.post(
    "/customers",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def add_customer(
    customer: CreateCustomer,
    db: Session = Depends(get_session),
):
    try:
        new_customer = crud.add_customer(db, customer)
        # Logando dados importantes
        logger.info(
            f"Cliente criado com sucesso: {new_customer.customer_name} (ID: {new_customer.customer_id})"
        )
        return new_customer
    except Exception as e:
        traceback.print_exc()
        # Logando o erro
        logger.error(f"Erro ao criar cliente: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# # Publica os dados do novo Cliente no RabbitMQ


# ROUTE GET CUSTOMER FROM CUSTOMERS
@router.get("/customers/{customer_id}", response_model=None)
def get_customer(customer_id, db: Session = Depends(get_session)):

    customer = crud.get_customer_by_id(db, customer_id)
    if not customer:
        logger.warning(f"Cliente não encontrado: ID {customer_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )

    logger.info(f"Cliente acessado: {customer.customer_name} (ID: {customer.customer_id})")
    return customer

# ROUTE EDIT CUSTOMER FROM CUSTOMERS
@router.put("/customers/{customer_id}", response_model=None)
def edit_customer(
    customer_id: int,
    customer: EditCustomer,
    db: Session = Depends(get_session),
):
    customer_updated = crud.edit_customer(db, customer_id, customer)
    if not customer_updated:
        logger.warning(
            f"Tentativa de atualização de cliente não encontrado: ID {customer_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )

    logger.info(
        f"Cliente atualizado com sucesso: {customer_updated.customer_name} (ID: {customer_updated.customer_id})"
    )
    return customer_updated

# # Publica os dados do Cliente editado no RabbitMQ

# ROUTE DELETE CUSTOMER FROM CUSTOMERS
@router.delete("/customers/{}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_session),
):
    if not crud.delete_customer(db, customer_id):
        logger.warning(
            f"Tentativa de deletação de cliente não encontrado: ID {customer_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )

    logger.info(f"Cliente deletado com sucesso: ID {customer_id}")
    return {"msg": "Produto deletado com sucesso."}

# # Publica Cliente deletado no RabbitMQ