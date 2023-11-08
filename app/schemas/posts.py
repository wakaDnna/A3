from pydantic import BaseModel, ConfigDict, field_validator,PydanticUserError
from typing import Optional
from uuid import UUID
from datetime import datetime
# from app.schemas.users import User

# class PostBase(BaseModel):
#    content: str
#    created_at: Optional[datetime] = None

#    model_config = ConfigDict(from_attributes=True)

class Post(BaseModel):
   id: int
   user_id: str
   content: str
   created_at: Optional[datetime] = None


   # user: Optional[User]

   # model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

   # @field_validator('id', 'user_id')
   # def check_fields(cls, v):
   #    return v

# class GetPost(PostBase):
#    id: int
#    user_id: str

#    @field_validator('id', 'user_id')
#    def check_fields(cls, v):
#       return v