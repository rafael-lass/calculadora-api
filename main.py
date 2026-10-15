from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.database import SessionLocal, Base, engine, get_db
from src.models import LogsCalculosModel
from src.scheema import LogsCalculos, LogsCalculosResponse

from typing import List

Base.metadata.create_all(bind=engine)


def gravar_log(operacao: str, n1: float, n2: float, n3:float):
        if n3 > 0:
            n3_bool = True
        else:
            n3_bool = False
            
        dados_validados = LogsCalculos(
            operacao_usada=operacao,
            primeiro_valor=n1,
            segundo_valor=n2,
            resultado=n3,
            maior_que_zero=n3_bool
        )
        
        db: Session = SessionLocal()
        
        try: 
            registro_db = LogsCalculosModel(**dados_validados.model_dump())
            db.add(registro_db)
            db.commit()
        except Exception as e:
            print(f"Erro ao salvar no banco: {e}")
            db.rollback()
        finally:
            db.close()

app = FastAPI()

@app.get("/")
def base(db: Session = Depends(get_db)):
    n = db.query(LogsCalculosModel).count()
    return {"Criador": "Rafael Lass",
            "Versão API": "1.0",
            "Quantidade de Registros":n}



@app.get("/soma/{n1}/{n2}")
def soma(n1: float, n2: float):
    '''Soma os primerio valor com segundo valor e armazena o resultado'''
    try:
        operacao = 'soma'
        n1 = float(n1)
        n2 = float(n2)
        n3 = n1 + n2
    except Exception as e:
        print('Erro')
    else:
        gravar_log(operacao, n1, n2, n3)
    return {'Resultado':n3}


@app.get("/subtracao/{n1}/{n2}")
def subtracao(n1: float, n2: float):
    '''Subtrai os primerio valor com segundo valor e armazena o resultado'''
    try:
        operacao = 'subtração'
        n1 = float(n1)
        n2 = float(n2)
        n3 = n1 - n2
    except Exception as e:
        print('Erro')
    else:
        gravar_log(operacao, n1, n2, n3)
        return {'Resultado':n3}
    
@app.get("/divisao/{n1}/{n2}")
def divisao(n1: float, n2: float):
    '''Soma os primerio valor com segundo valor e armazena o resultado'''
    if n1 == 0 or n2 == 0:
        return {'Erro': 'Não é possível dividir valores com 0'}
    try:
        operacao = 'soma'
        n1 = float(n1)
        n2 = float(n2)
        n3 = n1 / n2
    except Exception as e:
        print('Erro')
    else:
        gravar_log(operacao, n1, n2, n3)
    return {'Resultado':n3}
    
@app.get('/logs', response_model=List[LogsCalculosResponse])
def listar_logs(db: Session = Depends(get_db)):
    return db.query(LogsCalculosModel).all()