from sqlalchemy.orm import sessionmaker, Session
from models import StockModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG

def get_stock_by_id(db: Session, stock_id:int):
    return db.query(StockModel).filter(StockModel.stock_id == stock_id).first()

def get_stocks(db: Session):
    return db.query(StockModel).all()