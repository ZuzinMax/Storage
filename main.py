from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from src.schemas.ItemSchema import router as item_router
from src.schemas.PlaceSchema import router as place_router
from src.schemas.StorageSchema import router as storage_router


app = FastAPI(title="Storage")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(item_router)
app.include_router(place_router)
app.include_router(storage_router)