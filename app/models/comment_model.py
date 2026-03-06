from pydantic import BaseModel
from datetime import datetime


class CommentDB(BaseModel):
    post_id: str
    user_id: int
    text: str
    created_at: datetime