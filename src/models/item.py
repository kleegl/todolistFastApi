from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from src.database.database import Base


class Item(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Integer, default=0)
