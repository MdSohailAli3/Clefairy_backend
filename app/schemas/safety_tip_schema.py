from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# 1️ Shared fields
class SafetyTipBase(BaseModel):
    title: str
    description: str

# 2️ Used when creating a tip
class SafetyTipCreate(SafetyTipBase):
    pass

# 3 Used when updating
class SafetyTipUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# 4️ Used when returning data to app
class SafetyTipResponse(BaseModel):
    id: str
    title: str
    description: str
    videoUrl: str
    thumbnailUrl: Optional[str]
    createdAt: datetime