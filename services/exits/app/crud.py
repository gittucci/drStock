from sqlalchemy.orm import sessionmaker, Session
from models import ExitsModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG
def add_exit(db: Session, exit: BaseModel):
    new_exit = ExitsModel(**exit.dict())
    db.add(new_exit)
    db.commit()
    db.refresh(new_exit)
    return new_exit

def get_exit_by_id(db: Session, exit_id:int):
    return db.query(ExitsModel).filter(ExitsModel.exit_id == exit_id).first()

def get_exits(db: Session):
    return db.query(ExitsModel).all()

def edit_exit(db: Session, exit_id: int, exit_data: BaseModel):
    exit = get_exit_by_id(db, exit_id)
    if not exit:
        return None
    for key, value in exit_data.dict(exclude_unset=True).items():
        setattr(exit, key, value)
    db.commit()
    db.refresh(exit)
    return exit

def delete_exit(db: Session, exit_id: int):
    exit = get_exit_by_id(db, exit_id)
    if not exit:
        return False
    db.delete(exit)
    db.commit()
    return True