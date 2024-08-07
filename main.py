from fastapi import FastAPI
from .database import engine
from .routers import admin, user
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(user.router)
