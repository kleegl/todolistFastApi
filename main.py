import uvicorn

from fastapi import FastAPI, Query
from src.routes.items_router import router as items_router
from src.config.config import settings

app = FastAPI()
app.include_router(items_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.uvicorn_reload)
