from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime


class UserBase(BaseModel):
   id: str
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

class CreateUser(BaseModel):
   name: str
   display_id: str
   bio: Optional[str] = None

class UpdateUser(BaseModel):
   name: str
   display_id: str
   bio: str
   birthday: date

class DeleteUser(BaseModel):
   user_id: str
   name: str
   display_id: str
   