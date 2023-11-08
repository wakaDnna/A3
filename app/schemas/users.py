from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from uuid import UUID
from datetime import date, datetime

from app.models.posts import Post

class UserBase(BaseModel):
   name: str
   display_id: str
   bio: Optional[str] = None
   image: Optional[bytes] = None
   followers_count: Optional[int] = 0
   following_count: Optional[int] = 0
   birthday: Optional[date] = None
   created_at: Optional[datetime] = None
   updated_at: Optional[datetime] = None

   model_config = ConfigDict(from_attributes=True)

# class User(UserBase):
#    id: str
   # posts: Optional[List['Post']] = []
   