from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import cloudinary.uploader
from fastapi.concurrency import run_in_threadpool
from app.services.safety_tip_service import create_safety_tip, get_daily_safety_tip
from app.schemas.safety_tip_schema import  SafetyTipResponse
from datetime import datetime, timezone
router = APIRouter(prefix="/users/safety-tips", tags=["Safety-Tips"])

@router.post("/upload", response_model=SafetyTipResponse)
async def create_tip(
    title: str = Form(...),
    description: str = Form(...),
    video: UploadFile = File(...)
):
    try:
        # ✅ Validate file type
        if not video.content_type.startswith("video/"):
            raise HTTPException(status_code=400, detail="File must be a video")

        # Reset file pointer
        video.file.seek(0)

        # ✅ Run Cloudinary upload in threadpool (important)
        upload_result = await run_in_threadpool(
            cloudinary.uploader.upload,
            video.file,
            resource_type="video",
            folder="daily-safety-tips"
        )

        tip_data = {
            "title": title,
            "description": description,
            "videoUrl": upload_result["secure_url"],
            "thumbnailUrl": upload_result.get("secure_url") + ".jpg",
            "isActive": True,
            "createdAt": datetime.now(timezone.utc)
        }

        tip_id = await create_safety_tip(tip_data)

        return {
            "id": tip_id,
            "title": title,
            "description": description,
            "videoUrl": upload_result["secure_url"],
            "thumbnailUrl": upload_result.get("secure_url") + ".jpg",
            "createdAt": tip_data["createdAt"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/daily", response_model=SafetyTipResponse)
async def get_daily_tip():
    tip = await get_daily_safety_tip()

    if not tip:
        raise HTTPException(status_code=404, detail="No safety tip found")

    return tip