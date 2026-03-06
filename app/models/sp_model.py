from pydantic import BaseModel, EmailStr

class SPCreate(BaseModel):
    district: str
    sp_name: str
    office_phone: str
    email: EmailStr
    mobile: str


class SPUpdate(BaseModel):
    sp_name: str | None = None
    office_phone: str | None = None
    email: EmailStr | None = None
    mobile: str | None = None

class SPResponse(BaseModel):
    district: str
    sp_name: str
    office_phone: str
    email: EmailStr
    mobile: str

    class Config:
        orm_mode = True