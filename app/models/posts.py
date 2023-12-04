from sqlalchemy import Column, String, Integer, LargeBinary, Date, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# 投稿テーブル
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey("users.id"))
    like_count = Column(Integer, default=0)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())