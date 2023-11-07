from sqlalchemy import Column, String, Integer, LargeBinary, Text, text, Date, DateTime
from sqlalchemy_utils import UUIDType
from datetime import date, datetime
from database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    display_id = Column(String(50), nullable=False)
    bio = Column(String(255), nullable=True)
    image = Column(LargeBinary, nullable=True)
    followers_count = Column(Integer, nullable=True)
    following_count = Column(Integer, nullable=True)
    birthday = Column(Date, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

# class User(UserModel):
#     pass


# class CreateUser(UserModel):
#     pass

# class User(Base):
#    __tablename__ = "users"

#    id = Column(String(36), primary_key=True, default=func.uuid())
#    name = Column(String(50), nullable=False)
#    display_id = Column(String(50), nullable=False)
#    bio = Column(String, nullable=True)
#    image = Column(LargeBinary, nullable=True)
#    followers_count = Column(Integer, nullable=True)
#    following_count = Column(Integer, nullable=True)
#    birthday = Column(Date, nullable=True)
#    created_at = Column(DateTime, default=func.now())
#    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())