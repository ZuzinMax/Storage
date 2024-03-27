from sqlalchemy import insert, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from auth.database import get_async_session
from src.models.StorageModel import StorageModel, ReadStorage
from src.models.models import storage

router = APIRouter(
    prefix="/storage",
    tags=["Storage"]
)

@router.get("/read")
async def read_storage(place_name: ReadStorage, session: AsyncSession = Depends(get_async_session)):
    query = select(storage).where(storage.c.place == place_name)
    result = await session.execute(query)
    return result.all()

