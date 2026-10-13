from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes

Base.metadata.create_all(engine)




app = FastAPI(title = "This is my first FastAPI application", description = "This is a simple FastAPI application to demonstrate the basic functionality of FastAPI.", version = "1.0.0")
app.include_router(task_routes)