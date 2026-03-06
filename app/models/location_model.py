from pydantic import BaseModel
from datetime import datetime

class LocationPointDB(BaseModel):
    latitude: float
    longitude: float
    updated_at: datetime
