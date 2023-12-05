from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.users import User

class Follow(Base):
    __tablename__ = "follows"
    follower_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    following_id = Column(String(36), ForeignKey("users.id"), primary_key=True)

    follower = relationship('User', foreign_keys=[follower_id])
    following = relationship('User', foreign_keys=[following_id])
    