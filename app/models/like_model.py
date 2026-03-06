from pydantic import BaseModel
from datetime import datetime


class LikeDB(BaseModel):
    post_id: str
    user_id: int
    created_at: datetime