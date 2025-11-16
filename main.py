# место для написания основной логики API

from fastapi import FastAPI

app = FastAPI()

@app.get("/User")
def home() -> dict:
    return {
        "id":"1",
        "email":"admin@admin.com",
        "password":"Admin"
    }

