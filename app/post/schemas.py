from pydantic import BaseModel

class PostRequest(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    post_id: int
    title: str
    content: str