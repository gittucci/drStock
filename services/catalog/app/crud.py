from sqlalchemy.orm import sessionmaker, Session
from models import CatalogModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG
def add_product(db: Session, product: BaseModel):
    new_product = CatalogModel(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product_by_id(db: Session, product_id:int):
    return db.query(CatalogModel).filter(CatalogModel.product_id == product_id).first()

def get_products(db: Session):
    return db.query(CatalogModel).all()

def edit_product(db: Session, product_id: int, product_data: BaseModel):
    product = get_product_by_id(db, product_id)
    if not product:
        return None
    for key, value in product_data.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True