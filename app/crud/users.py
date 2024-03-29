from app.database import Session, get_db
from app.models.users import User
from app.models.posts import Post
from app.models.follows import Follow
from app.schemas.posts import PostBase, CreatePost
from app.schemas.users import CreateUser, UserBase, UpdateUser, DeleteUser
from fastapi import APIRouter, Depends
from typing import List

users_router = APIRouter()

@users_router.get('/users', tags=['User'], summary="ユーザ情報一覧を取得", description="ユーザの一覧を取得します", response_model=List[UserBase])
def get_users(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    print('[get_users] start')
    return db.query(User).offset(offset).limit(limit).all()

@users_router.get('/users/{user_id}', tags=['User'], summary="1件のユーザ情報を取得", description="ユーザIDからユーザ情報を検索します", response_model=UserBase)
def get_user(db: Session = Depends(get_db), user_id: str = ''):
    print('[get_user] start user_id:',user_id)
    if user_id == '':
        return None
    
    return db.query(User).filter(User.id == user_id).first()

@users_router.get('/users/{user_id}/posts', tags=['User'], summary="ユーザ投稿一覧取得", description="指定ユーザの投稿一覧を取得します", response_model=List[PostBase])
def read_posts_for_user(user_id: str, db: Session = Depends(get_db)):
    print('[START] read posts for user id:', user_id)
    return db.query(Post).filter(Post.user_id == user_id).all()

@users_router.post('/users', tags=['User'], summary="ユーザを新規作成", description="ユーザを新規作成します", response_model=UserBase)
def create_user(body: CreateUser, db: Session = Depends(get_db)):
    print('[create_users] start')
    user = User(
        name=body.name,
        display_id=body.display_id,
        bio=body.bio
    )
    db.add(user)
    db.commit()

    user = db.query(User).filter(User.name == body.name).first()

    return user

@users_router.post('/users/{user_id}/posts', tags=['User'], summary="新規投稿", description="新規に投稿を行います", response_model=List[PostBase])
def create_post(body: CreatePost, user_id: str, db: Session = Depends(get_db)):
    print('[START] create post')
    post = Post(
        user_id=user_id,
        content=body.content
    )
    db.add(post)
    db.commit()

    return db.query(Post).filter(Post.user_id == user_id).all()

@users_router.put('/users/{user_id}', tags=['User'], summary="ユーザ情報を更新", description="指定されたユーザIDのユーザ情報を更新します", response_model=UserBase)
def update_user(body: UpdateUser, id: str = '', db: Session = Depends(get_db)):
    print('[START] update user id:',id)

    user = db.query(User).filter(User.id == id).first()
    if user is None:
        return '該当データがありませんでした'
    
    user.name = body.name
    user.display_id = body.display_id
    user.bio = body.bio
    user.birthday = body.birthday
    db.commit()

    return user

@users_router.post('/users/{follower_id}/follow/{following_id}', tags=['User'], summary="ユーザをフォローします", description="ユーザをフォローします")
def follow_user(follower_id: str, following_id: str, db: Session = Depends(get_db)):
    print('[START] follow user')
    print(follower_id)
    print(following_id)

    follow = Follow(
        follower_id=follower_id,
        following_id=following_id
    )

    db.add(follow)
    db.commit()

    return db.query(Follow).filter(Follow.follower_id == follower_id).first()

@users_router.delete('/users/{user_id}', tags=['User'], summary="ユーザを削除", description="指定されたユーザIDのユーザ情報を削除します", response_model=DeleteUser)
def delete_user(db: Session = Depends(get_db), user_id: str = ''):
    print('[START] delete user id:',user_id)

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return '該当のユーザは存在しません'
    
    db.delete(user)
    db.commit()

    return user