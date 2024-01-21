from pydantic import BaseModel

class CreatePostRequest(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    post_id: int
    title: str
    content: str