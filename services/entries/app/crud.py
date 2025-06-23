from sqlalchemy.orm import sessionmaker, Session
from models import EntriesModel
from typing import List
from pydantic import BaseModel, EmailStr

# CRUD CATALOG
def add_entry(db: Session, entry: BaseModel):
    new_entry = EntriesModel(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_entry_by_id(db: Session, entry_id:int):
    return db.query(EntriesModel).filter(EntriesModel.entry_id == entry_id).first()

def get_entries(db: Session):
    return db.query(EntriesModel).all()

def edit_entry(db: Session, entry_id: int, entry_data: BaseModel):
    entry = get_entry_by_id(db, entry_id)
    if not entry:
        return None
    for key, value in entry_data.dict(exclude_unset=True).items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry

def delete_entry(db: Session, entry_id: int):
    entry = get_entry_by_id(db, entry_id)
    if not entry:
        return False
    db.delete(entry)
    db.commit()
    return True