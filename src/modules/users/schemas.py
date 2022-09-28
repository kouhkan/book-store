from abc import ABC

from pydantic import BaseModel
from pydantic import Field


class BaseUser(BaseModel, ABC):
    pass


class UserIn(BaseUser):
    name: str = Field(min_length=3, max_length=128)
    phone_number: str = Field(min_length=10, max_length=10)


class UserOut(BaseUser):
    id: int
    name: str

    class Config:
        orm_mode = True
