from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from database import Base

class SuppliersModel(Base):
    __tablename__ = "suppliers"
    
    supplier_id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    whatsapp = Column(String)
    cellphone = Column(String, nullable=False)
    telephone = Column(String)
    cpf_cnpj = Column(String, nullable=False)
    zipcode = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(String, nullable=False)
    complement = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    last_update = Column(DateTime, default=func.now())
    user_id = Column(Integer)