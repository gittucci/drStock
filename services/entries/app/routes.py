from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import EntriesModel
from database import SessionLocal

router = APIRouter()

@router.post("/entries/")
def add_entry(entry: EntriesModel):
    db: Session = SessionLocal()
    db.add(entry)
    db.commit()
    db.refresh(entry)
    db.close()
    return entry

@router.put("/entries/{entry_id}")
def edit_entry(entry_id: int, entry: EntriesModel):
    db: Session = SessionLocal()
    db_entry = db.query(EntriesModel).filter(EntriesModel.entries_id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    # Update entry fields here
    db.commit()
    db.close()
    return db_entry

@router.delete("/entries/{entry_id}")
def delete_entry(entry_id: int):
    db: Session = SessionLocal()
    db_entry = db.query(EntriesModel).filter(EntriesModel.entries_id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(db_entry)
    db.commit()
    db.close()
    return {"detail": "Entry deleted"}