from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import StockModel
from database import SessionLocal

router = APIRouter()

@router.get("/stock/")
def get_stock():
    db: Session = SessionLocal()
    stock = db.query(StockModel).all()
    for item in stock:
        item.stockQty = item.calculate_stock()  # Calculate stock
    db.close()
    return stock

@router.post("/stock/")
def add_stock(stock: StockModel):
    db: Session = SessionLocal()
    db.add(stock)
    db.commit()
    db.refresh(stock)
    db.close()
    return stock

@router.put("/stock/{stock_id}")
def edit_stock(stock_id: int, stock: StockModel):
    db: Session = SessionLocal()
    db_stock = db.query(StockModel).filter(StockModel.stock_id == stock_id).first()
    if not db_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    # Update entry fields here
    db.commit()
    db.close()
    return db_stock

@router.delete("/stock/{stock_id}")
def delete_stock(stock_id: int):
    db: Session = SessionLocal()
    db_stock = db.query(StockModel).filter(StockModel.stock_id == stock_id).first()
    if not db_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    db.delete(db_stock)
    db.commit()
    db.close()
    return {"detail": "Stock deleted"}