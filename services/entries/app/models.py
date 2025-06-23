from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy import func
from datetime import datetime
from pydantic import BaseModel, BaseSettings, Field
from database import Base
from typing import List, Optional

class EntriesModel(Base):
    __tablename__ = "entries"
    
    entry_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)    
    code = Column(String, nullable=False)
    barcode = Column(String, nullable=False) 
    description = Column(String)
    supplier_name = Column(String)
    restockPoint = Column(Integer)     
    restockCost = Column(Float)
    entryDate = Column(DateTime, nullable=False)  
    entryQty = Column(Integer, nullable=False)  
    totalEntries = Column(Integer, nullable=False)
    totalExits = Column(Integer, nullable=False)  
    unit = Column(String)
    stockPrice = Column(Float)
    stockLocation = Column(String)
    last_update = Column(DateTime, default=func.now())
    user_id = Column(Integer)

# ESQUEMA DE CRIAÇÃO
class CreateEntry(BaseModel):
    entry_id: int
    product_id: int 
    code: str
    barcode: str 
    description: str
    supplier_name: str
    restockPoint: int     
    restockCost: float
    entryDate: datetime  
    entryQty: int  
    totalEntries: int
    totalExits: int 
    unit: str
    stockPrice: float
    stockLocation: str
    last_update: datetime
    user_id: int
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

# ESQUEMA DE EDIÇÃO
class EditEntry(BaseModel):
    entry_id: Optional[int]
    product_id: Optional[int] 
    code: Optional[str]
    barcode: Optional[str] 
    description: Optional[str]
    supplier_name: Optional[str]
    restockPoint: Optional[int]     
    restockCost: Optional[float]
    entryDate: Optional[datetime]  
    entryQty: Optional[int]  
    totalEntries: Optional[int]
    totalExits: Optional[int] 
    unit: Optional[str]
    stockPrice: Optional[float]
    stockLocation: Optional[str]
    last_update: Optional[datetime]
    user_id: Optional[int]
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True