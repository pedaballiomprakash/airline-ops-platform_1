from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import flights

app = FastAPI()

# Enable CORS for frontend at localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api/health")
def health():
    return {"status": "ok"}

# Include flights router
app.include_router(flights.router)
