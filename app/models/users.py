from sqlalchemy import Column, String, Integer, LargeBinary, Date, DateTime
from sqlalchemy.sql import func
from database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(50), nullable=False)
    display_id = Column(String(50), nullable=False)
    bio = Column(String(255), nullable=True)
    image = Column(LargeBinary, nullable=True)
    followers_count = Column(Integer, nullable=True, default=0)
    following_count = Column(Integer, nullable=True, default=0)
    birthday = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
