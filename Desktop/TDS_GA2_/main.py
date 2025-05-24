from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks once at startup
with open("marks.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, None) for n in name]}
