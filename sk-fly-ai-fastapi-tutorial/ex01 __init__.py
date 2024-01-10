"""
https://fastapi.tiangolo.com/ko/
python -m pip install --upgrade pip
pip install fastapi
pip install uvicorn[standard]

실행 : uvicorn main:app --reload --port 8000
api 문서 확인 : http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}