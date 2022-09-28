import typing as t
from datetime import datetime

import inflection
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import sessionmaker

from src.config import Development
from utils.strings import to_snake_case

engine = create_engine(
    Development.SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


@declarative_mixin
class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return to_snake_case(inflection.pluralize(cls.__name__))

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, unique=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, unique=False, default=datetime.utcnow)


def create_or_modify_instance(model_instance: t.Mapping, data: t.Dict) -> t.Mapping:
    """Map a request schema to a model instance"""

    for key, value in data.__dict__.items():
        setattr(model_instance, key, value)
    return model_instance


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
