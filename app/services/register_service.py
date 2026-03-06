from app.db.mongodb import MongoManager
from app.services.aadhaar import encrypt_aadhar

async def add_user(data: dict):
    user_collection = MongoManager.get_collection("users")

    data["aadhaar"] = encrypt_aadhar(data["aadhaar"])

    # generate user_id safely
    last_user = await user_collection.find_one(
        {},
        sort=[("user_id", -1)]
    )

    if last_user:
        new_id = last_user["user_id"] + 1
    else:
        new_id = 100

    data["user_id"] = new_id

    await user_collection.insert_one(data)

    return new_id

