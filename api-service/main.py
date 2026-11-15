from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "api-service", "message": "Hello from the API"}

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Brian"},
        {"id": 2, "name": "Wanjiku"},
        {"id": 3, "name": "Otieno"},
    ]
