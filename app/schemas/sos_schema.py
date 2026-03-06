from pydantic import BaseModel

class SOSRequest(BaseModel):
    user_id: int
    name: str
    latitude: float
    longitude: float
