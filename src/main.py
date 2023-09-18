import uvicorn
from redis import asyncio as aioredis
from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from api.routers import all_routers
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from config import REDIS_HOST, REDIS_PORT
from fastapi_users import FastAPIUsers
from models.auth import Users
from auth.manager import get_user_manager


app = FastAPI(
    title="python_interview_preparation"
)


for router in all_routers:
    app.include_router(router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: Users = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
