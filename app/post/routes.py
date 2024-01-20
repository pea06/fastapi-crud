from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from .models import Post
from .schemas import CreatePostRequest

router = APIRouter()

@router.post("/create")
def create_post(
    request: CreatePostRequest, 
    db: Session = Depends(get_db)
    ):
    post = Post(
        title = request.title,
        content = request.content
    )

    db.add(post)
    db.commit()

    return { "success": True }