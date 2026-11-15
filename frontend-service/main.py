import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

API_URL = os.getenv("API_URL", "http://localhost:8001")

@app.get("/")
def home():
    return {"service": "frontend-service", "message": "Hello from the frontend"}

@app.get("/users")
def users():
    try:
        r = httpx.get(f"{API_URL}/users", timeout=5)
        return {"from": "frontend-service", "users": r.json()}
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Cannot reach api-service")
