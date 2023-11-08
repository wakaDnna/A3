from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_db, Session
from app.crud.posts import posts_router

app = FastAPI()

app.include_router(router=posts_router)

# @app.get('/users')
# def read_users(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, offset, limit)
#     return users


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)