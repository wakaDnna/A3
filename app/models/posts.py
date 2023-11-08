from sqlalchemy import Column, String, Integer, LargeBinary, Date, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import ConfigDict, PydanticUserError
from app.database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), ForeignKey("users.id"))
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    # users = relationship("User")