from app.db.mongodb import MongoManager
async def add_sp_service(data):
    sp_collection = MongoManager.get_collection("sp")
    existing = await sp_collection.find_one(
        {"district": data.district.upper()}
    )

    if existing:
        return None

    sp_data = data.dict()
    sp_data["district"] = data.district.upper()

    result = await sp_collection.insert_one(sp_data)
    return str(result.inserted_id)


async def update_sp_service(district, data):
    sp_collection = MongoManager.get_collection("sp")

    update_data = {
        k: v for k, v in data.dict().items() if v is not None
    }

    result = await sp_collection.update_one(
        {"district": district.upper()},
        {"$set": update_data}
    )

    return result.matched_count


async def get_sp_service(district):
    sp_collection = MongoManager.get_collection("sp")
    sp = await sp_collection.find_one(
        {"district": district.upper()},
        {"_id": 0}
    )
    return sp


async def get_all_sp_service():
    sp_collection = MongoManager.get_collection("sp")
    cursor = sp_collection.find({}, {"_id": 0})

    result = []
    async for doc in cursor:
        result.append(doc)

    return result

async def bulk_add_sp_service(sp_list):
    sp_collection = MongoManager.get_collection("sp")
    documents = []

    for sp in sp_list:
        data = sp.dict()
        data["district"] = data["district"].upper()
        documents.append(data)

    # remove districts already present
    districts = [doc["district"] for doc in documents]

    existing_cursor = sp_collection.find(
        {"district": {"$in": districts}},
        {"district": 1}
    )

    existing = [doc["district"] async for doc in existing_cursor]

    filtered_docs = [
        doc for doc in documents
        if doc["district"] not in existing
    ]

    if not filtered_docs:
        return 0

    result = await sp_collection.insert_many(filtered_docs)

    return len(result.inserted_ids)