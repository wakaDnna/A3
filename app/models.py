from sqlalchemy import Column, String, Integer, LargeBinary, Text, text, Date, DateTime
from sqlalchemy_utils import UUIDType
from datetime import date, datetime
from app.database import Base
import uuid


class UserBase(Base):
    __tablename__ = "users"
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)


class User(UserBase):
    name = Column(String(50))
    display_id = Column(String(50))
    bio = Column(Text)
    # image = Column(LargeBinary)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    birthday = Column(Date)
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)

    def __init__(self, name: str, display_id: str, bio: str, followers_count: int, following_count: int, birthday: date):
        self.name = name
        self.display_id = display_id
        self.bio = bio
        # self.image = image
        self.followers_count = followers_count
        self.following_count = following_count
        self.birthday = birthday
        # self.created_at = created_at
        # self.updated_at = updated_at


class CreateUser(User):
    pass
