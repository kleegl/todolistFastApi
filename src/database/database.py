from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config.config import settings

db_url = f"mssql+pyodbc://{settings.database_login}:{settings.database_pwd}@{settings.database_host}/{settings.database_name}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
