from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.routers import auth, flights

from app.core.config import settings
from app.database.db import get_db
from app.routers import flights

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Backend for the Airline Operations Management Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health", tags=["Health"])
def health():
    return {"status": "ok", "service": settings.PROJECT_NAME}


@app.get("/api/health/db", tags=["Health"])
def db_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "connected"}


app.include_router(auth.router, prefix=settings.API_V1_PREFIX)
app.include_router(flights.router)
app.include_router(flights.router)