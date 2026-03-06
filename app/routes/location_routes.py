from fastapi import APIRouter, HTTPException
from app.schemas.position import (
    LocationUpdate,
    LocationResponse
)
from app.services.live_location import (
    update_location,
    get_location
)

router = APIRouter(
    prefix="/location",
    tags=["Live-Location"]
)

@router.post("/update")
async def update(data: LocationUpdate):
    await update_location(data)
    return {"message": "Location updated"}


@router.get("/{user_id}", response_model=LocationResponse)
async def fetch(user_id: int):
    location = await get_location(user_id)
    if not location:
        raise HTTPException(
            status_code=404,
            detail="Location not found"
        )
    return location
