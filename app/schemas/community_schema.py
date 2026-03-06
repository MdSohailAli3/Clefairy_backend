from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


# ---------- POSTS ----------

# class PostCreate(BaseModel):
#     user_id: int
#     content: str = Field(..., min_length=1, max_length=500)


class PostResponse(BaseModel):
    post_id: str
    user_id: int
    # text optional, media only posts allowed
    content: Optional[str] = None

    media_url: Optional[str] = None
    media_type: Optional[str] = None  # image | video
    
    likes_count: int
    comments_count: int
    created_at: datetime


# ---------- COMMENTS ----------

class CommentCreate(BaseModel):
    user_id: int
    text: str = Field(..., min_length=1, max_length=300)


class CommentResponse(BaseModel):
    comment_id: str
    post_id: str
    user_id: int
    text: str
    created_at: datetime


# ---------- FEED ----------

class FeedResponse(BaseModel):
    posts: List[PostResponse]
    page: int # post sent in small chunks -> 1 page 1 to 10 posts, 2nd page 11 to 20 posts
    limit: int # post loads at a time