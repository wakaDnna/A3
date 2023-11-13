from pydantic import BaseModel, ConfigDict, field_validator,PydanticUserError
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
   id: int
   user_id: str
   content: str
   created_at: Optional[datetime] = None

class CreatePost(BaseModel):
   user_id: str
   content: str

class UpdatePost(BaseModel):
   content: str

class DeletePost(BaseModel):
   id: int
   user_id: str
   content: str