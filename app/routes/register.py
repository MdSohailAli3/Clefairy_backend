from fastapi import APIRouter
from app.schemas.user_schema import User
from app.services.register_service import add_user

router = APIRouter(prefix="/users", tags=["Register-User"])

@router.post("/register")
async def register_user(data: User):
    id = await add_user(data.model_dump())
    return {
            "message": "user added successfully",
            "user_id": id
            }

