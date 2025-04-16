# fastAPI como gateway usando httpx

from fastapi import FastAPI, HTTPException
from httpx import AsyncClient

# --- FastAPI App ---
app = FastAPI(title="Gateway API", version="1.0.0")

# --- Configuration ---
# Service URLs (These would typically come from environment variables or a service discovery mechanism)
backend_url_catalog = "http://localhost:8000"
backend_url_customers = "http://localhost:8001"
backend_url_entries = "http://localhost:8002"
backend_url_exits = "http://localhost:8003"
backend_url_stock = "http://localhost:8004"
backend_url_suppliers = "http://localhost:8005"
backend_url_authorization = "http://localhost:8006"
# Add more service URLs as needed

# --- API Gateway Routes ---
@app.get("/")
async def root():
    return {"message": "Welcome to the Gateway API"}

@app.get("/catalog/{path}")
async def catalog_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_catalog}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")

@app.get("/customers/{path}")
async def customers_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_customers}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")
        
@app.get("/entries/{path}")
async def entries_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_entries}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")        
        
@app.get("/exits/{path}")
async def exits_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_exits}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")
            
@app.get("/stock/{path}")
async def exits_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_stock}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")
            
@app.get("/suppliers/{path}")
async def exits_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{backend_url_suppliers}/{path}")
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=503, detail="Service Unavailable")      