# from pydantic import BaseModel
# # validates the request user made
# # check types, if type mismatch -> Fastapi responds - 422 Unprocessable Entity

# class ChatRequest(BaseModel):
#     message: str

from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str
    timestamp: datetime

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)