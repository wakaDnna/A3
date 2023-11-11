from app.database import Session, get_db
# import app.models.posts as models
# from app.schemas.posts import Post
from app.models.posts import Post
from fastapi import APIRouter, Depends

posts_router = APIRouter()

# @posts_router.get('/post', response_model=None)
# def get_post(db: Session, post_id: int):
#     print('[get_post] start post_id:',post_id)
#     post = db.query(Post).filter(Post.id == post_id).first()
#     print(post)

# def get_post_by_user(db: Session, user_id: str):
#     print('[get_user_by_user] start user_id:',user_id)
#     return db.query(models.Post).filter(models.Post.user_id == user_id).first()

@posts_router.get('/posts', response_model=None)
def get_posts(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    print('[get_posts] start')
    return db.query(Post).offset(offset).limit(limit).all()

# def create_post(db: Session, user_id: str, content: str):
#     print('[create_post] start')
#     db.add(models.Post(user_id, content))
#     db.commit()

#     return 'success'