# место для написания основной логики API

from fastapi import FastAPI
from api import auth

app = FastAPI()

app.include_router(auth.router)
