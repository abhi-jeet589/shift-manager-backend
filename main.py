from fastapi import FastAPI
from .core.models.User import User
from contextlib import asynccontextmanager
from .utils.database import init_db
from .core.routes import UserRouter

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def index():
    return {"Hello":"World"}

app.include_router(UserRouter.router)