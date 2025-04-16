from fastapi import FastAPI
from database import engine
from contextlib import asynccontextmanager

app = FastAPI()

# Recursos que precisam ser inicializados e finalizados
async def startup_event():
    print("Iniciando o microsserviço...")
    # Aqui você pode conectar ao banco de dados, configurar clientes, etc.
    # Exemplo:
    # app.state.database = await connect_to_database()
    pass

async def shutdown_event():
    print("Encerrando o microsserviço...")
    # Aqui você pode desconectar do banco de dados, fechar conexões, etc.
    # Exemplo:
    # await app.state.database.disconnect()
    pass

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_event()
    yield
    await shutdown_event()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Microsserviço FastAPI rodando!"}

# Outras rotas e lógica do seu microsserviço aqui...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
