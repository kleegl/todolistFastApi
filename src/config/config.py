from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()


class Settings(BaseModel):
    uvicorn_reload: bool = os.getenv("UVICORN_RELOAD", "true") == "true"
    database_host: str = os.getenv("SQLALCHEMY_DATABASE_HOST", "localhost")
    database_login: str = os.getenv("SQLALCHEMY_DATABASE_LOGIN", "sa")
    database_pwd: str = os.getenv("SQLALCHEMY_DATABASE_PWD", "passw0rd!")
    database_name: str = os.getenv("SQLALCHEMY_DATABASE_NAME", "test")

    def print_settings(self):
        print(f"UVICORN_RELOAD: {self.uvicorn_reload}")
        print(f"DATABASE_HOST: {self.database_host}")
        print(f"DATABASE_LOGIN: {self.database_login}")
        print(f"DATABASE_PWD: {self.database_pwd}")
        print(f"DATABASE_NAME: {self.database_name}")


settings = Settings()
