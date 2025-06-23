from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import EntriesModel, EditEntry, CreateEntry
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE ADD ENTRY IN ENTRIES
@router.post(
    "/entries",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def add_entry(
    entry: CreateEntry,
    db: Session = Depends(get_session),
):
    try:
        new_entry = crud.add_entry(db, entry)
        # Logando dados importantes
        logger.info(
            f"Entrada criada com sucesso: {new_entry.description} (ID: {new_entry.entry_id})"
        )
        return new_entry
    except Exception as e:
        traceback.print_exc()
        # Logando o erro
        logger.error(f"Erro ao criar entrada: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# # Publica os dados da nova Entrada no RabbitMQ


# ROUTE GET ENTRY FROM ENTRIES
@router.get("/entries/{entry_id}", response_model=None)
def get_entry(entry_id, db: Session = Depends(get_session)):

    entry = crud.get_entry_by_id(db, entry_id)
    if not entry:
        logger.warning(f"Entrada não encontrada: ID {entry_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Entrada não encontrada"
        )

    logger.info(f"Entrada acessada: {entry.description} (ID: {entry.entry_id})")
    return entry

# ROUTE EDIT ENTRY FROM ENTRIES
@router.put("/entries/{entry_id}", response_model=None)
def edit_entry(
    entry_id: int,
    entry: EditEntry,
    db: Session = Depends(get_session),
):
    entry_updated = crud.edit_entry(db, entry_id, entry)
    if not entry_updated:
        logger.warning(
            f"Tentativa de atualização de Entrada não encontrada: ID {entry_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Entrada não encontrada"
        )

    logger.info(
        f"Entrada atualizada com sucesso: {entry_updated.description} (ID: {entry_updated.entry_id})"
    )
    return entry_updated

# # Publica os dados do ??? editado no RabbitMQ

# ROUTE DELETE ENTRY FROM ENTRIES
@router.delete("/entries/{}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(
    entry_id: int,
    db: Session = Depends(get_session),
):
    if not crud.delete_entry(db, entry_id):
        logger.warning(
            f"Tentativa de deletação de entrada não encontrada: ID {entry_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Entrada não encontrada"
        )

    logger.info(f"Entrada deletada com sucesso: ID {entry_id}")
    return {"msg": "Entrada deletada com sucesso."}

# # Publica ??? deletado no RabbitMQ