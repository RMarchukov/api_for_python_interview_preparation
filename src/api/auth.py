from fastapi import APIRouter
from services.auth import fastapi_users, auth_backend, client, SECRET
from schemas.auth import UserRead, UserCreate, UserUpdate


auth_routers = APIRouter()


auth_routers.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

auth_routers.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

auth_routers.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)

auth_routers.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth"],
)

auth_routers.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)

auth_routers.include_router(
    fastapi_users.get_oauth_router(client, auth_backend, SECRET),
    prefix="/auth/google",
    tags=["Auth"],
)
