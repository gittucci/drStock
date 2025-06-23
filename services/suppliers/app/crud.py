from sqlalchemy.orm import sessionmaker, Session
from models import SuppliersModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG
def add_supplier(db: Session, supplier: BaseModel):
    new_supplier = SuppliersModel(**supplier.dict())
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier

def get_supplier_by_id(db: Session, supplier_id:int):
    return db.query(SuppliersModel).filter(SuppliersModel.supplier_id == supplier_id).first()

def get_suppliers(db: Session):
    return db.query(SuppliersModel).all()

def edit_supplier(db: Session, supplier_id: int, supplier_data: BaseModel):
    supplier = get_supplier_by_id(db, supplier_id)
    if not supplier:
        return None
    for key, value in supplier_data.dict(exclude_unset=True).items():
        setattr(supplier, key, value)
    db.commit()
    db.refresh(supplier)
    return supplier

def delete_supplier(db: Session, supplier_id: int):
    supplier = get_supplier_by_id(db, supplier_id)
    if not supplier:
        return False
    db.delete(supplier)
    db.commit()
    return True