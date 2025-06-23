from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import ExitsModel, EditExit, CreateExit
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE ADD EXIT IN EXITS
@router.post(
    "/exits",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def add_exit(
    exit: CreateExit,
    db: Session = Depends(get_session),
):
    try:
        new_exit = crud.add_exit(db, exit)
        # Logando dados importantes
        logger.info(
            f"Saida criada com sucesso: {new_exit.description} (ID: {new_exit.exit_id})"
        )
        return new_exit
    except Exception as e:
        traceback.print_exc()
        # Logando o erro
        logger.error(f"Erro ao criar Saida: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# # Publica os dados da nova Saida no RabbitMQ


# ROUTE GET EXIT FROM EXITS
@router.get("/exits/{exit_id}", response_model=None)
def get_exit(exit_id, db: Session = Depends(get_session)):

    exit = crud.get_exit_by_id(db, exit_id)
    if not exit:
        logger.warning(f"Saida não encontrada: ID {exit_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Saida não encontrada"
        )

    logger.info(f"Saida acessada: {exit.description} (ID: {exit.exit_id})")
    return exit

# ROUTE EDIT EXIT FROM EXITS
@router.put("/exits/{exit_id}", response_model=None)
def edit_exit(
    exit_id: int,
    exit: EditExit,
    db: Session = Depends(get_session),
):
    exit_updated = crud.edit_exit(db, exit_id, exit)
    if not exit_updated:
        logger.warning(
            f"Tentativa de atualização de Saida não encontrada: ID {exit_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Saida não encontrada"
        )

    logger.info(
        f"Saida atualizada com sucesso: {exit_updated.description} (ID: {exit_updated.exit_id})"
    )
    return exit_updated

# # Publica os dados da Saida editada no RabbitMQ

# ROUTE DELETE EXIT FROM EXITS
@router.delete("/exits/{}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exit(
    exit_id: int,
    db: Session = Depends(get_session),
):
    if not crud.delete_exit(db, exit_id):
        logger.warning(
            f"Tentativa de deletação de Saida não encontrada: ID {exit_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Saida não encontrada"
        )

    logger.info(f"Saida deletada com sucesso: ID {exit_id}")
    return {"msg": "Saida deletada com sucesso."}

# # Publica Saida deletada no RabbitMQ