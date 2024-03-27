from sqlalchemy import insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from auth.database import get_async_session
from src.models.PlaceModel import AddPlace
from src.models.models import places

router = APIRouter(
    prefix="/operation_place",
    tags=["PLaces"]
)

@router.post("/add_place")
async def add_place(new_place: AddPlace, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(places).values(**new_place.dict())
    await session.execute(stmt)
    await session.commit()
    return {"Status": "success"}

@router.post("/del_place")
async def delete_item(place_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(places).where(places.c.place_id == place_id)
    await session.execute(stmt)
    await session.commit()
    return {"Status": "success"}