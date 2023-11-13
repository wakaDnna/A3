from app.database import Session, get_db
# import app.models.posts as models
# from app.schemas.posts import Post
from app.models.posts import Post
from fastapi import APIRouter, Depends

posts_router = APIRouter()

@posts_router.get('/posts', tags=['Post'], response_model=None)
def get_posts(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    print('[get_posts] start')
    return db.query(Post).offset(offset).limit(limit).all()

@posts_router.get('/posts/{post_id}', tags=['Post'], response_model=None)
def get_post(db: Session = Depends(get_db), id:int = 0):
    print('[START] get post id:',id)
    return db.query(Post).filter(Post.id == id).first()

@posts_router.post('/posts/{post_id}', tags=['Post'], response_model=None)
def create_post(db: Session = Depends(get_db), user_id: str = '', content: str = ''):
    print('[START] create post')
    post = Post(
        user_id=user_id,
        content=content
    )
    db.add(post)
    db.commit()

    return db.query(Post).filter(Post)

@posts_router.put('/posts/{post_id}', tags=['Post'], response_model=None)
def update_post(db: Session = Depends(get_db), post_id: int = 0, content: str = ''):
    print('[START] update post id:',post_id)

    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return '該当の投稿がありませんでした'
    
    post.content = content
    db.commit()

    return post

@posts_router.delete('/posts/{post_id}', tags=['Post'], response_model=None)
def delete_post(db: Session = Depends(get_db), post_id: int = 0):
    print('[START] delete post id: ',post_id)

    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return '該当の投稿が見つかりませんでした'
    
    db.delete(post)
    db.commit()

    return 'Deleted Post id=' + post_id
