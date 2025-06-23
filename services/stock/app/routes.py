from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_session
import crud
from models import StockModel
from loggerconfig import logger
import traceback
from pydantic import BaseSettings, Field
# from producers import get_rabbit_connection
import aio_pika
import json
import os

router = APIRouter()

# ROUTE GET STOCK FROM STOCK
@router.get("/stock/{stock_id}", response_model=None)
def get_stock(stock_id, db: Session = Depends(get_session)):

    stock = crud.get_stock_by_id(db, stock_id)
    if not stock:
        logger.warning(f"Estoque não encontrado: ID {stock_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Estoque não encontrado"
        )

    logger.info(f"Estoque acessado: {stock.description} (ID: {stock.stock_id})")
    return stock