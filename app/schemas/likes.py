from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LikeBase(BaseModel):
    id: int
    user_id: str
    post_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CreateLike(BaseModel):
    user_id: str