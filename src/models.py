from sqlalchemy import Column,Integer, Float, DateTime, Boolean, func, String
from src.database import Base

class LogsCalculosModel(Base):
    '''Modelo ORM para armazenar dados dos calculos'''
    
    __tablename__ = 'logs_calculos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    feito_em = Column(DateTime(timezone=True), server_default=func.now())
    operacao_usada= Column(String(10), nullable=False, index=True)
    primeiro_valor= Column(Float, nullable=False, index=True)
    segundo_valor= Column(Float, nullable=False, index=True)
    resultado =Column(Float, nullable=False, index=True)
    maior_que_zero =  Column(Boolean, nullable=False, index=True)