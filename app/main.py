from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine
import sys
from datetime import date, datetime


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
# app.include_router(users.router, tags=['User'])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        print('db started.')
        yield db
    finally:
        db.close()

origins = ["*"]

@app.get("/users", response_model=schemas.User)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print(sys.path)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.put("/user")
def create_user(name: str, display_id: str, bio: str, followers_count: int, following_count: int, birthday: date, db: Session = Depends(get_db)):
    user = crud.create_user(db, name=name, display_id=display_id, bio=bio, followers_count=followers_count, following_count=following_count, birthday=birthday)
    print(user)
    return user

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)