from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy import func
from datetime import datetime
from pydantic import BaseModel, BaseSettings, Field
from database import Base
from typing import List, Optional

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

# ESQUEMA DE CRIAÇÃO
class CreateSupplier(BaseModel):
    supplier_id: int
    supplier_name: str
    email: str
    whatsapp: str
    cellphone: str
    telephone: str
    cpf_cnpj: str
    zipcode: str
    street: str
    number: str
    complement: str
    city: str
    state: str
    country: str
    last_update: datetime
    user_id: int
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

# ESQUEMA DE EDIÇÃO
class EditSupplier(BaseModel):
    supplier_id: Optional[int]
    supplier_name: Optional[str]
    email: Optional[str]
    whatsapp: Optional[str]
    cellphone: Optional[str]
    telephone: Optional[str]
    cpf_cnpj: Optional[str]
    zipcode: Optional[str]
    street: Optional[str]
    number: Optional[str]
    complement: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    last_update: Optional[datetime]
    user_id: Optional[int]
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True