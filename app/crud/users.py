from app.database import Session, get_db
from app.models.users import User
from fastapi import APIRouter, Depends

users_router = APIRouter()

@users_router.get('/users', response_model=None)
def get_users(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    print('[get_users] start')
    return db.query(User).offset(offset).limit(limit).all()

@users_router.get('/user', response_model=None)
def get_user(db: Session = Depends(get_db), user_id: str = ''):
    print('[get_user] start user_id:',user_id)
    if user_id == '':
        return None
    
    return db.query(User).filter(User.id == user_id).first()

@users_router.put('/user', response_model=None)
def create_user(db: Session = Depends(get_db), name: str = '', display_id: str = '', bio: str = ''):
    print('[create_users] start')
    user = User(
        name=name,
        display_id=display_id,
        bio=bio
    )
    db.add(user)
    db.commit()

    user = db.query(User).filter(User.name == name).first()

    return user

@users_router.post('/user', response_model=None)
def update_user(db: Session = Depends(get_db), id: str = '', name:str = ''):
    print('[START] update user id:',id)

    user = db.query(User).filter(User.id == id).first()
    if user is None:
        return '該当データがありませんでした'
    
    user.name = name
    db.commit()

    return user

@users_router.delete('/user', response_model=None)
def delete_user(db: Session = Depends(get_db), id: str = ''):
    print('[START] delete user id:',id)

    user = db.query(User).filter(User.id == id).first()
    if user is None:
        return '該当のユーザは存在しません'
    
    db.delete(user)
    db.commit()

    return 'Deleted User id=' + id