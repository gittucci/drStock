# fastAPI como gateway usando httpx
import httpx
from httpx import AsyncClient
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from contextlib import asynccontextmanager
import asyncio
import json

app = FastAPI(
    title="API Gateway",
    description="Gateway para rotear requisições para APIs de backend",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

# Service URLs / APIs de backend
BACKEND_URL_CATALOG = "http://catalog_backend:8000"
BACKEND_URL_CUSTOMERS = "http://customers_backend:8001"
BACKEND_URL_ENTRIES = "http://entries_backend:8002"
BACKEND_URL_EXITS = "http://exits_backend:8003"
BACKEND_URL_STOCK = "http://stock_backend:8004"
BACKEND_URL_SUPPLIERS = "http://suppliers_backend:8005"

# Cliente HTTP assíncrono para fazer requisições para os backends
# É recomendável usar um Global Client em aplicações FastAPI
# para reuso de conexões e melhor performance.
# Pode ser inicializado em um evento de startup.
http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    """Fecha o cliente HTTP quando a aplicação é encerrada."""
    await http_client.aclose()

# ROTAS CATÁLOGO PRODUTOS
@app.api_route("/api/v1/productcatalog/{path:path}", methods=["POST"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/productcatalog/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/productcatalog/{path:path}", methods=["PUT"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/productcatalog/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/productcatalog/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/productcatalog/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/productcatalog/{path:path}", methods=["DELETE"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/productcatalog/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/productcatalog/{path:path}", methods=["PATCH"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/productcatalog/{path}"
    return await forward_request(request, target_url)

# ROTAS CLIENTES
@app.api_route("/api/v1/customers/{path:path}", methods=["POST"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/customers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/customers/{path:path}", methods=["PUT"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/customers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/customers/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/customers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/customers/{path:path}", methods=["DELETE"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/customers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/customers/{path:path}", methods=["PATCH"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/customers/{path}"
    return await forward_request(request, target_url)

# ROTAS ENTRADAS
@app.api_route("/api/v1/entries/{path:path}", methods=["POST"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/entries/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/entries/{path:path}", methods=["PUT"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/entries/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/entries/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/entries/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/entries/{path:path}", methods=["DELETE"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/entries/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/entries/{path:path}", methods=["PATCH"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/entries/{path}"
    return await forward_request(request, target_url)

# ROTAS SAIDAS
@app.api_route("/api/v1/exits/{path:path}", methods=["POST"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/exits/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/exits/{path:path}", methods=["PUT"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/exits/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/exits/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/exits/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/exits/{path:path}", methods=["DELETE"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/exits/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/exits/{path:path}", methods=["PATCH"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/exits/{path}"
    return await forward_request(request, target_url)

# ROTAS ESTOQUE
@app.api_route("/api/v1/stock/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/stock/{path}"
    return await forward_request(request, target_url)

# ROTAS FORNECEDORES
@app.api_route("/api/v1/suppliers/{path:path}", methods=["POST"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/suppliers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/suppliers/{path:path}", methods=["PUT"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/suppliers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/suppliers/{path:path}", methods=["GET"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/suppliers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/suppliers/{path:path}", methods=["DELETE"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/suppliers/{path}"
    return await forward_request(request, target_url)
@app.api_route("/api/v1/suppliers/{path:path}", methods=["PATCH"])
async def route_to_catalog_api(path: str, request: Request):
    target_url = f"{BACKEND_URL_CATALOG}/api/v1/suppliers/{path}"
    return await forward_request(request, target_url)

# REDIRECIONAMENTO PARA AS APIs DE BACKEND
async def forward_request(request: Request, target_url: str):
    """
    Função auxiliar para encaminhar a requisição original para o backend.
    Preserva o método HTTP, headers (exceto alguns sensíveis) e corpo da requisição.
    """

    try:
        # Prepara os headers para a requisição de saída
        # Remove headers que podem causar problemas ou são irrelevantes para o backend
        headers = {key: value for key, value in request.headers.items() if key.lower() not in ["host", "content-length", "transfer-encoding"]}

        # Lê o corpo da requisição de forma assíncrona
        body = await request.body()
        print(f"[{request.method}] Gateway - Forwarding: Headers={headers}, Body={body.decode()}") # Novo log

        # Faz a requisição ao backend
        response = await http_client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body,
            params=request.query_params,
            # Configurações de timeout para evitar espera infinita
            timeout=30.0
        )
        # Adicione log para a resposta REAL que o gateway recebe do backend
        print(f"[{request.method}] Gateway - Resposta do Backend: Status={response.status_code}, Content-Type={response.headers.get('content-type')}, Text={response.text}") # Novo log

        # Retorna a resposta do backend, incluindo status code e headers
        # Remove headers que o FastAPI irá adicionar ou que são de conexão
        response_headers = {key: value for key, value in response.headers.items() if key.lower() not in ["content-encoding", "transfer-encoding", "content-length"]}
        
        if response.headers.get("content-type", "").startswith("application/json"):
            return JSONResponse(
                content=response.json(),
                status_code=response.status_code,
                headers=response_headers
            )
        else:
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=response_headers,
                media_type=response.headers.get("content-type")
            )

    except httpx.ConnectError:
        print(f"[{request.method}] Gateway - ConnectError para {target_url}") # Novo log
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Não foi possível conectar à API de backend em {target_url}. Verifique se ela está em execução."
        )
    except httpx.TimeoutException:
        print(f"[{request.method}] Gateway - TimeoutException para {target_url}") # Novo log
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=f"A API de backend em {target_url} demorou muito para responder."
        )
    except Exception as e:
        print(f"[{request.method}] Gateway - Erro Inesperado: {e} para {target_url}") # Novo log
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro inesperado no gateway ao processar a requisição para {target_url}: {e}"
        )

# Rota padrão para testar se o gateway está ativo
@app.get("/")
async def read_root():
    return {"message": "API Gateway is running!"}