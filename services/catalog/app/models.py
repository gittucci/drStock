from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class CatalogModel(Base):
    __tablename__ = "productcatalog"
    
    product_id = Column(UUID, primary_key=True, index=True)
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