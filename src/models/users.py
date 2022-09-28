import enum

from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import String

from utils.database import Base
from utils.database import BaseModel


class UserRoles(enum.Enum):
    ADMIN = 1
    USER = 2


class User(BaseModel, Base):
    name = Column(String(length=128), nullable=False, unique=False)
    phone_number = Column(String(length=10), nullable=False, unique=True)
    role = Column(Enum(UserRoles), nullable=False, unique=False, default=UserRoles.USER.name)
