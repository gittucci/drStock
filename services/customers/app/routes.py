from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import CustomersModel
from database import SessionLocal

router = APIRouter()

@router.post("/customers/")
def add_customer(customer: CustomersModel):
    db: Session = SessionLocal()
    db.add(customer)
    db.commit()
    db.refresh(customer)
    db.close()
    return customer

@router.put("/customers/{customer_id}")
def edit_customer(customer_id: int, customer: CustomersModel):
    db: Session = SessionLocal()
    db_customer = db.query(CustomersModel).filter(CustomersModel.customer_id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    # Update customer fields here
    db.commit()
    db.close()
    return db_customer

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    db: Session = SessionLocal()
    db_customer = db.query(CustomersModel).filter(CustomersModel.customer_id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    db.close()
    return {"detail": "Customer deleted"}