from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.models.item import Item
from src.dto.item_dto import Item_Dto
from src.database.database import get_db

router = APIRouter(tags=["Item"])


@router.get("/get_item/{id}", response_model=Item_Dto)
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found."
        )
    return item


@router.post("/create_item/", response_model=Item_Dto)
def create_item(item_dto: Item_Dto, db: Session = Depends(get_db)):
    item = Item(**item_dto.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item.id


@router.put("/update_item/{id}", response_model=Item_Dto)
def update_item(id: int, item_dto: Item_Dto, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        raise HTTPException("Item not found.")
    for key, value in item_dto.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/delete_item/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    item_db = db.query(Item).filter(Item.id == id).first()
    if item_db is None:
        raise HTTPException("Item not found.")
    db.delete(item_db)
    db.commit()
    return status.HTTP_200_OK
