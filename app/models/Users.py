from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import relationship

from database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    display_id = Column(String(50), unique=True)
    bio = Column(String)
    image = Column(MEDIUMBLOB)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    birthday = Column(Date)
