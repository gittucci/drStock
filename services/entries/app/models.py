from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from database import Base

class EntriesModel(Base):
    __tablename__ = "entries"
    
    entries_id = Column(Integer, primary_key=True, index=True)
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