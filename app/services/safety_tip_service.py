from app.db.mongodb import MongoManager
from datetime import datetime, timezone
from bson import ObjectId

async def create_safety_tip(data: dict):
    safety_tip_collection = MongoManager.get_collection("safety_tips")

    data["createdAt"] = datetime.now(timezone.utc)
    result = await safety_tip_collection.insert_one(data)
    return str(result.inserted_id)

async def get_daily_safety_tip():
    safety_tip_collection = MongoManager.get_collection("safety_tips")
    cursor = safety_tip_collection.aggregate([
        {"$match": {"isActive": True}},   # filter active tips
        {"$sample": {"size": 1}}          # pick 1 random document
    ])

    tip = await cursor.to_list(length=1)

    if tip:
         tip = tip[0]
         return {
            "id": str(tip["_id"]),
            "title": tip["title"],
            "description": tip["description"],
            "videoUrl": tip["videoUrl"],
            "thumbnailUrl": tip.get("thumbnailUrl"),
            "createdAt": tip["createdAt"]
        }

    return None