from pydantic import BaseModel
from database import engineconn
from models import Chatbot
from fastapi import FastAPI

app = FastAPI()
engine = engineconn()
session = engine.sessionmaker()

@app.get("/chatbot")
async def first_get():
    example = session.query(Chatbot).all()
    return example