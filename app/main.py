from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crud.posts import posts_router
from app.crud.users import users_router

app = FastAPI()

app.include_router(router=posts_router)
app.include_router(router=users_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)