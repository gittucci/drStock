from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from database import Base

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