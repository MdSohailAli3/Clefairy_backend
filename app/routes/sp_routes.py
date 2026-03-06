from fastapi import APIRouter, HTTPException
from app.models.sp_model import SPCreate, SPUpdate, SPResponse
from app.services.sp_service import (
    add_sp_service,
    update_sp_service,
    get_sp_service,
    get_all_sp_service,
    bulk_add_sp_service
)
from typing import List
router = APIRouter(prefix="/sp", tags=["Rajasthan SP"])

@router.post("/add")
async def add_sp(data: SPCreate):

    result = await add_sp_service(data)

    if result is None:
        raise HTTPException(400, "SP already exists")

    return {"message": "SP added successfully", "id": result}

@router.put("/update/{district}")
async def update_sp(district: str, data: SPUpdate):

    matched = await update_sp_service(district, data)

    if matched == 0:
        raise HTTPException(404, "District not found")

    return {"message": "SP updated successfully"}


@router.get("/{district}", response_model=SPResponse)
async def get_sp(district: str):

    sp = await get_sp_service(district)

    if not sp:
        raise HTTPException(404, "SP not found")

    return sp

@router.get("/")
async def get_all_sp():
    return await get_all_sp_service() # list of documents, each document is a dict with sp details


@router.post("/bulk-add")
async def bulk_add_sp(data: List[SPCreate]):

    inserted_count = await bulk_add_sp_service(data)

    return {
        "message": "Bulk insert completed",
        "inserted": inserted_count
    }