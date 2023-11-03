from sqlalchemy.orm import Session
import app.models as models
from datetime import date, datetime


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    print('[get_users] start')
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, name: str, display_id: str, bio: str, followers_count: int, following_count: int, birthday: date):
    print('[create_users] start')
    db.add(models.User(name, display_id, bio, followers_count, following_count, birthday))
    db.commit()

    return 'insert'