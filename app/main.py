from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    a = 100
    b = "qwe"
    return {"message": "hello"}

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
    uvicorn.run(app, host="0.0.0.0", port=8000)