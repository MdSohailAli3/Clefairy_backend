from pydantic import BaseModel

class User(BaseModel):
    name: str
    contact: str
    email: str
    aadhaar: str