from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")

async def read_item(item_id: str, q: Optional[str] = None): # q : 생략 가능

    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}