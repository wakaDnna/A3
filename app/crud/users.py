from sqlalchemy.orm import Session
import app.models as models
from datetime import date, datetime


def get_user(db: Session, user_id: str):
    print('[get_user] start user_id:',user_id)
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    print('[get_user_by_name] start name:',name)
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, offset: int = 0, limit: int = 100):
    print('[get_users] start ')
    return db.query(models.User).offset(offset).limit(limit).all()

def create_user(db: Session, name: str, display_id: str):
    print('[create_users] start')
    db.add(models.User(name, display_id))
    db.commit()

    return 'success'