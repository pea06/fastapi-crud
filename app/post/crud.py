from typing import List, Optional

from sqlalchemy.orm import Session

from .schemas import PostRequest
from .models import Post

def get_post(post_id: int, db: Session,) -> Optional[Post]:
    return db.query(Post).filter_by(post_id = post_id).first()

def get_posts(db: Session) -> List[Post]:
    return db.query(Post).all()

def create_post(request: PostRequest, db: Session):
    post = Post(
        title = request.title, 
        content = request.content
    )

    db.add(post)
    db.commit()

def delete_post(post_id: int, db: Session):
    post = get_post(post_id, db)
    db.delete(post)
    db.commit()

def update_post(post_id: int, request: PostRequest, db: Session):
    post = db.query(Post).filter_by(post_id=post_id).first()

    if post:
        post.title = request.title
        post.content = request.content
        db.commit()