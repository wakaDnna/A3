from app.database import Session, get_db
from app.models.posts import Post
from fastapi import APIRouter, Depends

posts_router = APIRouter()

@posts_router.get('/posts', tags=['Post'], summary="全ての投稿を取得", description="全ての投稿を取得します", response_model=None)
def get_posts(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    print('[get_posts] start')
    return db.query(Post).offset(offset).limit(limit).all()

@posts_router.get('/posts/{post_id}', tags=['Post'], summary="1件の投稿内容を取得", description="指定された投稿IDの投稿内容を取得します", response_model=None)
def get_post(db: Session = Depends(get_db), id:int = 0):
    print('[START] get post id:',id)
    return db.query(Post).filter(Post.id == id).first()

@posts_router.post('/posts', tags=['Post'], summary="新規投稿", description="新規に投稿を行います", response_model=None)
def create_post(db: Session = Depends(get_db), user_id: str = '', content: str = ''):
    print('[START] create post')
    post = Post(
        user_id=user_id,
        content=content
    )
    db.add(post)
    db.commit()

    return db.query(Post).all()

@posts_router.put('/posts/{post_id}', tags=['Post'], summary="投稿内容を更新", description="指定された投稿の内容を更新します", response_model=None)
def update_post(db: Session = Depends(get_db), post_id: int = 0, content: str = ''):
    print('[START] update post id:',post_id)

    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return '該当の投稿がありませんでした'
    
    post.content = content
    db.commit()

    return post

@posts_router.delete('/posts/{post_id}', tags=['Post'], summary="投稿を削除", description="指定された投稿を削除します", response_model=None)
def delete_post(db: Session = Depends(get_db), post_id: int = 0):
    print('[START] delete post id: ',post_id)

    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return '該当の投稿が見つかりませんでした'
    
    db.delete(post)
    db.commit()

    return {"message": "Deleted Post", "post_id": post.id}
