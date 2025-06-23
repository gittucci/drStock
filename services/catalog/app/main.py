from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from database import get_session, engine, Base
from contextlib import asynccontextmanager
import routes
from slowapi import Limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from pydantic import BaseSettings, Field
from loggerconfig import logger
from starlette.responses import JSONResponse
import os

# Inicializando a aplicação FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_event()
    yield
    await shutdown_event()

app = FastAPI(
    title="API de Exemplo - FastAPI",
    version="1.0",
    description="Esta é a API do microsserviço CATALOG.",
    openapi_url="/api/v1/openapi.json",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Microsserviço CATALOG rodando!"}

# Rota para verificação de saúde da aplicação
@app.get("/healthz")
def healthz():
    return {"mensagem": "A aplicação CATALOG está saudável."}

# LIMITER - - - - - - - - - - - - - - - - - - - -
limiter = Limiter(key_func=get_remote_address)

# Adicionando o handler para rate limit excedido
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Tratamento customizado para quando o limite for excedido
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    logger.warning(
        f"Rate limit excedido para {request.client.host} no endpoint {request.url.path}"
    )  # Log de aviso
    return JSONResponse(
        status_code=429,
        content={"message": "Muitas requisições, tente novamente mais tarde."},
    )

# Recursos que precisam ser inicializados e finalizados
async def startup_event():
    print("Iniciando o microsserviço CATALOG ...")
    app.state.database = get_session() # tirei o await
    Base.metadata.create_all(bind=engine)
    logger.info("Tabelas do banco de dados criadas com sucesso.")
    logger.info("Inicialização da aplicação CATALOG ...") 

async def shutdown_event():
    print("Encerrando o microsserviço CATALOG ...")
    await app.state.database.disconnect()
    logger.info("Fechamento da aplicação CATALOG ...") 

# ROTAS - - - - - - - - - - - - - - - - - - - -
app.include_router(routes.router, prefix="/api/v1", tags=["API v1"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)