from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from .crud import get_post, create_post, get_posts
from .schemas import CreatePostRequest, PostResponse

router = APIRouter()

@router.post("/create")
def create_post_endpoint(
    request: CreatePostRequest, 
    db: Session = Depends(get_db)
    ):
    create_post(request, db)

    return { "success": True }

@router.get("/list")
def get_posts_endpoint(
    db: Session = Depends(get_db)
    ) -> List[PostResponse]:

    posts = get_posts(db)

    return [PostResponse(post_id=post.post_id, title=post.title, content=post.content) for post in posts]

@router.get("/{post_id}")
def get_post_endpoint(
    post_id: int,
    db: Session = Depends(get_db)
    ) -> PostResponse:
    
    post = get_post(post_id, db)

    return PostResponse(
        post_id = post.post_id,
        title = post.title,
        content = post.content
    )
    