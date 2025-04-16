from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import ExitsModel
from database import SessionLocal

router = APIRouter()

@router.post("/exits/")
def add_exit(exit: ExitsModel):
    db: Session = SessionLocal()
    db.add(exit)
    db.commit()
    db.refresh(exit)
    db.close()
    return exit

@router.put("/exits/{exit_id}")
def edit_exit(exit_id: int, exit: ExitsModel):
    db: Session = SessionLocal()
    db_exit = db.query(ExitsModel).filter(ExitsModel.exits_id == exit_id).first()
    if not db_exit:
        raise HTTPException(status_code=404, detail="Exit not found")
    # Update exit fields here
    db.commit()
    db.close()
    return db_exit

@router.delete("/exits/{exit_id}")
def delete_exit(exit_id: int):
    db: Session = SessionLocal()
    db_exit = db.query(ExitsModel).filter(ExitsModel.exits_id == exit_id).first()
    if not db_exit:
        raise HTTPException(status_code=404, detail="Exit not found")
    db.delete(db_exit)
    db.commit()
    db.close()
    return {"detail": "Exit deleted"}