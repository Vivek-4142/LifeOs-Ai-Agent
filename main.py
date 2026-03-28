from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LifeOs Ai - Agent-Based Email Management System", version="1.0")

app.include_router(router)