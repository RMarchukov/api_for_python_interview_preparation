from typing import Optional
from fastapi import Depends, Request
from models.auth import Users, get_user_db
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas, FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from config import SECRET, CLIENT_ID, CLIENT_SECRET
from httpx_oauth.clients.google import GoogleOAuth2


SECRET = SECRET

client = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)


class UserManager(IntegerIDMixin, BaseUserManager[Users, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, users: Users, request: Optional[Request] = None):
        print(f"User {users.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)
