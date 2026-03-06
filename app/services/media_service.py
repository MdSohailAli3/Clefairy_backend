import cloudinary.uploader
from fastapi import UploadFile


async def upload_media(file: UploadFile):

    # read file bytes
    file_bytes = await file.read()

    resource_type = "auto"  
    # auto detects image or video

    result = cloudinary.uploader.upload(
        file_bytes,
        resource_type=resource_type,
        folder="community_posts"
    )

    return {
        "url": result["secure_url"],
        "public_id": result["public_id"],
        "resource_type": result["resource_type"]
    }