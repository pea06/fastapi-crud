from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .post.routes import router as post_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router, prefix="/post")