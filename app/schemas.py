from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

# class UserBase(BaseModel):
#     name: str
#     display_id: str
#     bio: str
#     image: bytes
#     followers_count: int
#     following_count: int
#     birthday: date
#     created_at: datetime
#     updated_at: datetime

class User(BaseModel):
    id: str
    name: str
    display_id: str
    bio: str
    image: bytes
    followers_count: int
    following_count: int
    birthday: date
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CreateUser(User):
    id: str
    name: str
    display_id: str
    bio: str
    # image: bytes
    followers_count: int
    following_count: int
    birthday: date
    # created_at: datetime
    # updated_at: datetime
