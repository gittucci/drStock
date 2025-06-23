from sqlalchemy.orm import sessionmaker, Session
from models import CustomersModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG
def add_customer(db: Session, customer: BaseModel):
    new_customer = CustomersModel(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer_by_id(db: Session, customer_id:int):
    return db.query(CustomersModel).filter(CustomersModel.customer_id == customer_id).first()

def get_customers(db: Session):
    return db.query(CustomersModel).all()

def edit_customer(db: Session, customer_id: int, customer_data: BaseModel):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        return None
    for key, value in customer_data.dict(exclude_unset=True).items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        return False
    db.delete(customer)
    db.commit()
    return True