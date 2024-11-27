import os
from dotenv import load_dotenv

load_dotenv()

reload = os.getenv("UVICORN_RELOAD", "false").lower() == "true"