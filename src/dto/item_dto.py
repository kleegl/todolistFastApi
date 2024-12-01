from pydantic import BaseModel


class Item_Dto(BaseModel):
    title: str
    author: str
    description: str | None
    priority: int = 0
