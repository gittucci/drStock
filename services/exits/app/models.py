from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy import func
from datetime import datetime
from pydantic import BaseModel, BaseSettings, Field
from database import Base
from typing import List, Optional

class ExitsModel(Base):
    __tablename__ = "exits"
    
    exits_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)    
    code = Column(String, nullable=False)
    barcode = Column(String, nullable=False) 
    description = Column(String)
    customer_id = Column(Integer, nullable=False)     
    customer_name = Column(String)
    exitDate = Column(DateTime, nullable=False)  
    exitQty = Column(Integer, nullable=False)    
    totalExits = Column(Integer, nullable=False)  
    unit = Column(String)
    stockPrice = Column(Float)
    stockLocation = Column(String)
    last_update = Column(DateTime, default=func.now())
    user_id = Column(Integer)

# ESQUEMA DE CRIAÇÃO
class CreateExit(BaseModel):
    exits_id: int
    product_id: int   
    code: str
    barcode: str 
    description: str
    customer_id: int     
    customer_name: str
    exitDate: datetime  
    exitQty: int    
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
class EditExit(BaseModel):
    exits_id: Optional[int]
    product_id: Optional[int]   
    code: Optional[str]
    barcode: Optional[str] 
    description: Optional[str]
    customer_id: Optional[int ]    
    customer_name: Optional[str]
    exitDate: Optional[datetime]
    exitQty: Optional[int]  
    totalExits: Optional[int]
    unit: Optional[str]
    stockPrice: Optional[float]
    stockLocation: Optional[str]
    last_update: Optional[datetime]
    user_id: Optional[int]
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True