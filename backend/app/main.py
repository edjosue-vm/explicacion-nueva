from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routers import explanations, interactions
from app.services.firebase_service import initialize_firebase

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Vivid Explanations API",
    description="Motor de Explicaciones Adaptativas - Backend API",
    version="1.0.0"
)

# CORS configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase
initialize_firebase()

# Include routers
app.include_router(explanations.router, prefix="/api/explanations", tags=["explanations"])
app.include_router(interactions.router, prefix="/api/interactions", tags=["interactions"])

@app.get("/")
async def root():
    return {
        "message": "Vivid Explanations API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}