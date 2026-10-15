from pydantic import BaseModel, ConfigDict
from datetime import datetime

class LogsCalculos(BaseModel):
    '''Scheema de validação de dados para inserir no banco de dados'''
    operacao_usada: str
    primeiro_valor: float
    segundo_valor: float
    resultado: float
    maior_que_zero: bool

class LogsCalculosResponse(LogsCalculos):
    
    id: int
    feito_em: datetime
    
    model_config = ConfigDict(from_attributes=True)