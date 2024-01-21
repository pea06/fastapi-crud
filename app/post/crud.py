from typing import List, Optional

from sqlalchemy.orm import Session

from .schemas import CreatePostRequest
from .models import Post

def get_post(post_id: int, db: Session,) -> Optional[Post]:
    return db.query(Post).filter_by(post_id = post_id).first()

def get_posts(db: Session) -> List[Post]:
    return db.query(Post).all()

def create_post(request: CreatePostRequest, db: Session):
    post = Post(
        title = request.title, 
        content = request.content
    )

    db.add(post)
    db.commit()