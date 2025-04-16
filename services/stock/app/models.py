from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class StockModel(Base):
    __tablename__ = "stock"
    
    stock_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)    
    code = Column(String, nullable=False)
    barcode = Column(String, nullable=False) 
    description = Column(String)
    supplier_name = Column(String)
    restockPoint = Column(Integer)     
    cost = Column(Float)
    stockAtualDate = Column(DateTime, nullable=False)  
    stockQty = Column(Integer, nullable=False)
    inventoryDate = Column(DateTime, nullable=False)  
    inventoryQty = Column(Integer, nullable=False)
    totalEntries = Column(Integer, nullable=False)
    totalExits = Column(Integer, nullable=False)    
    unit = Column(String)
    stockPrice = Column(Float)
    stockLocation = Column(String)
    last_update = Column(DateTime, default=func.now())
    user_id = Column(Integer)

    def calculate_inventory(self):  # refazer


    def calculate_stock(self):  # refazer
        total_entries = sum(entry.quantity for entry in self.entries)
        total_exits = sum(exit.quantity for exit in self.exits)
        return total_entries - total_exits