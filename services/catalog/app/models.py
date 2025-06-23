from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy import func
from datetime import datetime
from pydantic import BaseModel, BaseSettings, Field
from database import Base
from typing import List, Optional

class CatalogModel(Base):
    __tablename__ = "productcatalog"
 
    product_id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    barcode = Column(String, nullable=False) 
    description = Column(String)
    supplier_id = Column(Integer)    
    supplier_name = Column(String)
    restockPoint = Column(Integer)     
    cost = Column(Float)
    unit = Column(String)
    stockPrice = Column(Float)
    stockLocation = Column(String)
    last_update = Column(DateTime, default=func.now())
    user_id = Column(Integer)

# ESQUEMA DE CRIAÇÃO
class CreateProduct(BaseModel):
    product_id: int
    code: str
    barcode: str
    description: str
    supplier_id: int
    supplier_name: str
    restockPoint: int
    cost: float
    unit: str
    stockPrice: float
    stockLocation: str
    last_update: datetime
    user_id: int
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

# ESQUEMA DE EDIÇÃO
class EditProduct(BaseModel):
    product_id: Optional[int]   
    code: Optional[str]
    barcode: Optional[str]
    description: Optional[str]
    supplier_id: Optional[int]
    supplier_name: Optional[str]
    restockPoint: Optional[int]
    cost: Optional[float]
    unit: Optional[str]
    stockPrice: Optional[float]
    stockLocation: Optional[str]
    last_update: Optional[datetime]
    user_id: Optional[int]
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True