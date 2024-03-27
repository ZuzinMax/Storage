from sqlalchemy import insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from auth.database import get_async_session
from src.models.ItemModel import AddItem
from src.models.models import items

router = APIRouter(
    prefix="/operation_item",
    tags=["Items"]
)

@router.post("/add_item")
async def add_item(new_item: AddItem, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(items).values(**new_item.dict())
    await session.execute(stmt)
    await session.commit()
    return {"Status": "success"}

@router.post("/del_item")
async def delete_item(item_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(items).where(items.c.item_id == item_id)
    await session.execute(stmt)
    await session.commit()
    return {"Status": "success"}