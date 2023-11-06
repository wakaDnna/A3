from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import User
from app.schemas import  UserBase, UserCreate
from app.database import get_db

from fastapi_crudrouter import SQLAlchemyCRUDRouter


app = FastAPI()
router = SQLAlchemyCRUDRouter(
    schema=UserBase,
    create_schema=UserCreate,
    db_model=User,
    db=get_db,
)
app.include_router(router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)