from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostDB(BaseModel):
    user_id: int

    # text is optional now (media-only posts allowed)
    content: Optional[str] = None

    # media fields
    media_url: Optional[str] = None
    media_type: Optional[str] = None   # "image" | "video"

    # engagement counters
    likes_count: int = 0
    comments_count: int = 0

    # timestamps
    created_at: datetime
    updated_at: datetime