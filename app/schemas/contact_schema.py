from pydantic import BaseModel, Field
# from typing import List

class EmergencyContact(BaseModel):
    user_id: int #new
    name: str = Field(..., min_length=2) # field is used for validation
    phone: str = Field(..., min_length=10, max_length=13) # 13 for additional +91
    relation: str
