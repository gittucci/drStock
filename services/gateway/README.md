fastAPI como Gateway

fastAPI como gateway usando httpx
Essa é uma combinação para construir microsserviços e APIs que agregam dados de múltiplas fontes.

1.  **FastAPI como Receptor:** 
Seu aplicativo FastAPI atuará como o ponto de entrada para os clientes (aplicativos front-end, outros serviços, etc.). Ele definirá as rotas da sua API de gateway.
2.  **httpx para Requisições Backend:** 
Dentro das suas rotas FastAPI, você usará a biblioteca `httpx` para fazer requisições HTTP para os seus serviços backend.
3.  **Agregação e Transformação:** 
O FastAPI receberá as respostas dos serviços backend, poderá agregá-las, transformá-las (se necessário) e, em seguida, retornar uma única resposta unificada para o cliente.

**Vantagens de usar FastAPI e httpx como gateway:**

* **Desempenho:** 
FastAPI é construído sobre Starlette e Pydantic, oferecendo alto desempenho. `httpx` também é uma biblioteca HTTP assíncrona eficiente.
* **Concorrência:** 
FastAPI suporta programação assíncrona (`async` e `await`), o que é ideal para lidar com múltiplas requisições simultâneas aos serviços backend sem bloquear o thread principal. `httpx` também é projetado para operações assíncronas.
* **Validação e Serialização:** 
O Pydantic integrado ao FastAPI facilita a validação dos dados de entrada e a serialização das respostas, tanto para as requisições do cliente quanto para as respostas dos serviços backend (embora você possa precisar definir seus próprios modelos para os dados backend).
* **Facilidade de Uso:** 
FastAPI é conhecido por sua sintaxe concisa e intuitiva, o que torna o desenvolvimento mais rápido e agradável. `httpx` também tem uma API amigável.
* **Suporte a HTTP/2 e HTTP/3:** 
`httpx` oferece suporte a protocolos HTTP mais recentes, o que pode melhorar a performance das comunicações com seus serviços backend.
* **Testabilidade:** 
FastAPI é projetado com a testabilidade em mente, facilitando a criação de testes para o seu gateway.

**Exemplo Básico:**

```python
from fastapi import FastAPI
from httpx import AsyncClient

app = FastAPI()
backend_url_produto = "http://servico-produto/produtos"
backend_url_preco = "http://servico-preco/precos"

@app.get("/produto/{produto_id}")
async def get_produto_detalhes(produto_id: int):
    async with AsyncClient() as client:
        try:
            produto_response = await client.get(f"{backend_url_produto}/{produto_id}")
            produto_response.raise_for_status()  # Levanta uma exceção para erros HTTP

            preco_response = await client.get(f"{backend_url_preco}/{produto_id}")
            preco_response.raise_for_status()

            produto_data = produto_response.json()
            preco_data = preco_response.json()

            return {
                "id": produto_data["id"],
                "nome": produto_data["nome"],
                "descricao": produto_data["descricao"],
                "preco": preco_data["valor"]
            }
        except Exception as e:
            return {"erro": f"Erro ao buscar detalhes do produto: {e}"}

```

**Considerações Importantes:**

* **Tratamento de Erros:** 
Implemente um tratamento de erros robusto para lidar com falhas nas requisições aos serviços backend (timeouts, erros de rede, erros HTTP).
* **Timeouts:** 
Configure timeouts adequados para as requisições `httpx` para evitar que o gateway fique preso esperando por respostas dos serviços backend.
* **Logging:** 
Implemente logging para monitorar as requisições e respostas do gateway e dos serviços backend.
* **Segurança:** 
Considere a segurança nas comunicações entre o gateway e os serviços backend (por exemplo, TLS/SSL, autenticação).
* **Transformação de Dados:** 
Se os formatos de dados dos serviços backend forem diferentes do que o cliente espera, você precisará realizar a transformação adequada no seu gateway.
* **Orquestração (Casos Mais Complexos):** 
Para fluxos de trabalho mais complexos envolvendo múltiplos serviços, você pode considerar o uso de ferramentas de orquestração de serviços. No entanto, para casos mais simples de agregação, FastAPI e httpx são suficientes.

Em resumo, usar FastAPI como um gateway com httpx para se comunicar com serviços backend é uma arquitetura **excelente e recomendada** para construir sistemas distribuídos e microsserviços.

**Exemplo Complexo:**
import fastapi
import httpx
import asyncio
from typing import Optional
from fastapi import Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl, constr
import logging
import sys

# --- Configuration ---
# Service URLs (These would typically come from environment variables or a service discovery mechanism)
SERVICE_A_URL = "http://localhost:8001"  #  Make sure these match your service URLs
SERVICE_B_URL = "http://localhost:8002"
# Add more service URLs as needed

# --- Logging ---
# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# --- FastAPI App ---
app = fastapi.FastAPI()

# --- HTTPX Client ---
# Create a single async client for the application.  This is good practice for performance.
async def get_http_client() -> httpx.AsyncClient:
    async with httpx.AsyncClient() as client:
        yield client

# Dependency to get the client
async def get_client(client: httpx.AsyncClient = Depends(get_http_client)):
    return client

# --- Data Models ---
# Example data models (define as needed for your API Gateway)
class GenericResponse(BaseModel):
    """
    Generic response model for consistent API responses.
    """
    status_code: int
    message: Optional[str] = None
    data: Optional[dict] = None
    error: Optional[str] = None

# --- Helper Functions ---

async def make_request(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    params: dict = None,
    json: dict = None,
    headers: dict = None,
    timeout: float = 10.0  # Add a timeout
) -> httpx.Response:
    """
    Helper function to make HTTP requests with error handling and logging.
    """
    try:
        logger.debug(f"Making {method} request to {url} with params={params}, json={json}, headers={headers}")
        response = await client.request(
            method,
            url,
            params=params,
            json=json,
            headers=headers,
            timeout=timeout, # Use the timeout here
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response
    except httpx.TimeoutException as e:
        logger.error(f"Timeout error: {e}")
        raise HTTPException(status_code=408, detail="Request timed out") from e
    except httpx.HTTPError as e:
        logger.error(f"HTTP error: {e}, Response content: {e.response.text if e.response else 'No response'}")
        # Improved error handling:  Return the error detail from the target service if available
        detail = f"Service {url} error: {e.response.json().get('detail') if e.response and e.response.content else str(e)}"
        status_code = e.response.status_code if e.response else 500
        raise HTTPException(status_code=status_code, detail=detail) from e
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}") from e

# --- API Gateway Routes ---

@app.get("/")
async def root():
    """
    Default root endpoint.
    """
    return GenericResponse(status_code=200, message="API Gateway is running")

@app.get("/service-a/")
async def get_service_a(
    client: httpx.AsyncClient = Depends(get_client),
    param_a: Optional[str] = Query(None, description="Parameter for Service A"),
    param_b: Optional[int] = Query(None, description="Another parameter for Service A")
):
    """
    Route to proxy requests to Service A.  Example with query parameters.
    """
    url = f"{SERVICE_A_URL}/"  # Adjust the path as needed for service A
    params = {}
    if param_a:
        params["param_a"] = param_a
    if param_b:
        params["param_b"] = param_b

    response = await make_request(client, "GET", url, params=params)
    return JSONResponse(content=response.json(), status_code=response.status_code) # Explicitly handle status code


@app.post("/service-b/")
async def post_service_b(
    client: httpx.AsyncClient = Depends(get_client),
    request_data: dict = fastapi.Body(..., description="Data to send to Service B"),
):
    """
    Route to proxy POST requests to Service B.  Example with a JSON body.
    """
    url = f"{SERVICE_B_URL}/process/"  # Adjust the path for Service B
    response = await make_request(client, "POST", url, json=request_data)
    return JSONResponse(content=response.json(), status_code=response.status_code)

# Example of handling a 404.  This shows how to customize error handling.
@app.get("/service-a/resource/{resource_id}")
async def get_service_a_resource(
    resource_id: int,
    client: httpx.AsyncClient = Depends(get_client),
):
    """
    Example route to get a specific resource from Service A.  Handles 404s.
    """
    url = f"{SERVICE_A_URL}/resource/{resource_id}"
    response = await make_request(client, "GET", url)
    return JSONResponse(content=response.json(), status_code=response.status_code)

# Example of a more complex proxy, passing headers and handling different methods
@app.route("/proxy/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_generic(
    path: str,
    request: fastapi.Request,
    client: httpx.AsyncClient = Depends(get_client),
):
    """
    Generic proxy route to forward requests to a specified service.  This is very flexible.
    """
    # Determine the target service URL based on the path or some other logic
    if path.startswith("service-a/"):
        target_url = f"{SERVICE_A_URL}/{path.replace('service-a/', '', 1)}"
    elif path.startswith("service-b/"):
        target_url = f"{SERVICE_B_URL}/{path.replace('service-b/', '', 1)}"
    else:
        raise HTTPException(status_code=404, detail=f"Target service for path '{path}' not found")

    # Extract headers to forward (filter out internal FastAPI headers)
    headers = {k: v for k, v in request.headers.items() if k.lower() not in ["host", "connection", "content-length", "content-type"]}

    # Read the request body (if any)
    body = await request.body()
    json_body = None
    try:
        json_body = await request.json() # Use this, and remove the body=body
    except ValueError:
        pass #  It's not JSON, so we'll send the raw body

    method = request.method
    logger.info(f"Proxying {method} request to {target_url}, headers: {headers}, body: {body}, json_body: {json_body}") # Added logging
    response = await make_request(client, method, target_url, headers=headers, json=json_body if json_body else None, data=body if not json_body else None) # Adjusted

    #  Return the response as a StreamingResponse to handle various content types correctly
    return JSONResponse(content=response.json(), status_code=response.status_code)
