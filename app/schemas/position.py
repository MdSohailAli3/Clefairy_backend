from pydantic import BaseModel
from datetime import datetime
from typing import List


# request from mobile/app
class LocationUpdate(BaseModel):
    user_id: int
    latitude: float
    longitude: float


# single coordinate point
class LocationPoint(BaseModel):
    latitude: float
    longitude: float
    updated_at: datetime | None = None


# API response
class LocationResponse(BaseModel):
    user_id: int
    last_location: LocationPoint | None
    history: List[LocationPoint] = []
