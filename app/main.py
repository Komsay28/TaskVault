from fastapi import FastAPI
from app.db import Base, engine
from app.models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task vault is running!"}

@app.get("/health")
def health():
    return {"status":"ok"}