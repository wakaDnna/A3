from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
  id: Optional[str] = None
  name: str
  display_id: str
  bio: Optional[str] = None
  image: Optional[bytes] = None
  followers_count: Optional[int] = None
  following_count: Optional[int] = None
  birthday: Optional[date] = None
  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()

class UserCreate(UserBase):
  pass

class User(UserBase):
  id: str
  created_at: datetime
  updated_at: datetime

  class Config:
      orm_mode = True
