from fastapi import FastAPI
from src.config.uvicorn_config import *
import uvicorn


app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id: int):
    response = {
        "message": "hello",
        "item_id": f"{item_id}",
        "type": f"{type(item_id)}"
    }
    return response

@app.get("/items/{skip}/{limit}")
async def getFromCount(skip: int, limit: int):
    return f"skip = {skip} limit 111= {limit}"

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
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=reload)