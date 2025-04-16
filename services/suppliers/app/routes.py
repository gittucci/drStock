from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import SuppliersModel
from database import SessionLocal

router = APIRouter()

@router.post("/suppliers/")
def add_supplier(supplier: SuppliersModel):
    db: Session = SessionLocal()
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    db.close()
    return supplier

@router.put("/suppliers/{supplier_id}")
def edit_supplier(supplier_id: int, supplier: SuppliersModel):
    db: Session = SessionLocal()
    db_supplier = db.query(SuppliersModel).filter(SuppliersModel.supplier_id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    # Update supplier fields here
    db.commit()
    db.close()
    return db_supplier

@router.delete("/suppliers/{supplier_id}")
def delete_supplier(supplier_id: int):
    db: Session = SessionLocal()
    db_supplier = db.query(SuppliersModel).filter(SuppliersModel.supplier_id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db.delete(db_supplier)
    db.commit()
    db.close()
    return {"detail": "Supplier deleted"}