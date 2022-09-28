from fastapi import FastAPI

from src.modules import __all__ as modules
from utils.database import Base
from utils.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Store",
    version="0.0.1",
    description="Book Store a monolith project by FastAPI.",
)

for module in modules:
    app.include_router(module.router)
