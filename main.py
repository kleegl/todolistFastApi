import uvicorn

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
from src.config.uvicorn_config import reload


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get("/items")
async def read_items(q: Annotated[str | None, Query(max_length=60)] = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


@app.get("/items/{item_id}")
async def root(item_id: int):
    response = {"message": "hello", "item_id": f"{item_id}", "type": f"{type(item_id)}"}
    return response


@app.get("/items/{skip}/{limit}")
async def getFromCount(skip: int, limit: int):
    return f"skip = {skip} limit 111= {limit}"


@app.post("/create_item")
async def create_item(item: Item):
    return item


@app.post("/")
async def post():
    return None


@app.put("/")
async def put():
    return None


@app.delete("/")
async def delete():
    return None


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=reload)
