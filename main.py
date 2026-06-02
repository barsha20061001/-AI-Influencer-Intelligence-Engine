import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.services.data_service import get_influencers

app = FastAPI(title="Ratefluencer AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ratefluencer AI Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/influencers")
def influencers():
    return get_influencers()