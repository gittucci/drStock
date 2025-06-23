from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import SuppliersModel, EditSupplier, CreateSupplier
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE ADD SUPPLIER IN SUPPLIERS
@router.post(
    "/suppliers",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def add_supplier(
    supplier: CreateSupplier,
    db: Session = Depends(get_session),
):
    try:
        new_supplier = crud.add_supplier(db, supplier)
        # Logando dados importantes
        logger.info(
            f"Fornecedor criado com sucesso: {new_supplier.supplier_name} (ID: {new_supplier.supplier_id})"
        )
        return new_supplier
    except Exception as e:
        traceback.print_exc()
        # Logando o erro
        logger.error(f"Erro ao criar Fornecedor: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# # Publica os dados do novo ??? no RabbitMQ


# ROUTE GET SUPPLIER FROM SUPPLIERS
@router.get("/suppliers/{supplier_id}", response_model=None)
def get_supplier(supplier_id, db: Session = Depends(get_session)):

    supplier = crud.get_supplier_by_id(db, supplier_id)
    if not supplier:
        logger.warning(f"Fornecedor não encontrado: ID {supplier_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado"
        )

    logger.info(f"Fornecedor acessado: {supplier.supplier_name} (ID: {supplier.supplier_id})")
    return supplier

# ROUTE EDIT SUPPLIER FROM SUPPLIERS
@router.put("/suppliers/{supplier_id}", response_model=None)
def edit_supplier(
    supplier_id: int,
    supplier: EditSupplier,
    db: Session = Depends(get_session),
):
    supplier_updated = crud.edit_supplier(db, supplier_id, supplier)
    if not supplier_updated:
        logger.warning(
            f"Tentativa de atualização de Fornecedor não encontrado: ID {supplier_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado"
        )

    logger.info(
        f"Fornecedor atualizado com sucesso: {supplier_updated.supplier_name} (ID: {supplier_updated.supplier_id})"
    )
    return supplier_updated

# # Publica os dados do Fornecedor editado no RabbitMQ

# ROUTE DELETE SUPPLIER FROM SUPPLIERS
@router.delete("/suppliers/{}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_session),
):
    if not crud.delete_supplier(db, supplier_id):
        logger.warning(
            f"Tentativa de deletação de Fornecedor não encontrado: ID {supplier_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado"
        )

    logger.info(f"Fornecedor deletado com sucesso: ID {supplier_id}")
    return {"msg": "Fornecedor deletado com sucesso."}

# # Publica Fornecedor deletado no RabbitMQ