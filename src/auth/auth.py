from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

SECRET = "1b5c33df0110f4dccefdcb8930f3b8e22865f51844b165078b98edc6f546c1ef"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
