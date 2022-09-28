import os

from dotenv import load_dotenv

load_dotenv()


class Base:
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_USER"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_PORT = os.environ["DB_PORT"]
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Development(Base):
    pass


class Production(Base):
    pass


class Testing(Base):
    pass
