import uvicorn
from redis import asyncio as aioredis
from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from api.routers import all_routers
from config import REDIS_HOST, REDIS_PORT
import logging


logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title="python_interview_preparation"
)


for router in all_routers:
    app.include_router(router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
