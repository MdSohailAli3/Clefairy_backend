from datetime import datetime, UTC
from app.db.mongodb import MongoManager


async def update_location(data):
    loc = MongoManager.get_collection("location")
    # create coordinate point
    point = {
        "latitude": data.latitude,
        "longitude": data.longitude,
        "updated_at": datetime.now(UTC)
    }

    # check for same location update
    doc = await loc.find_one(
        {"_id": data.user_id}, 
        {"last_location": 1}
        )

    if doc and doc.get("last_location"):
        last = doc["last_location"]
        if (
            last["latitude"] == data.latitude and
            last["longitude"] == data.longitude
        ):
            return True

    # update Mongo document
    await loc.update_one(
        {"_id": data.user_id},
        {
            # store latest position (fast lookup)
            "$set": {
                "last_location": point
            },

            # append to history
            "$push": {
                "history": {
                    "$each": [point],
                    "$slice": -500   # keep last 500 points only
                }
            }
        },
        upsert=True
    )
    return True

async def get_location(user_id: int):
    loc = MongoManager.get_collection("location")
    doc = await loc.find_one({"_id": user_id})

    if not doc:
        return None

    return {
        "user_id": doc["_id"],
        "last_location": doc.get("last_location"),
        "history": doc.get("history",[])
    }

