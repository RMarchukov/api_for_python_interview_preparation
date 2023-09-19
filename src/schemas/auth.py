from typing import Union
from fastapi_users import schemas
from fastapi_users.schemas import model_dump
from pydantic import EmailStr, BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: Union[str, None]

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: Union[str, None]
    email: EmailStr
    password: str

    def create_update_dict(self):
        return model_dump(self)


class UserUpdate(schemas.BaseUserUpdate):
    pass
