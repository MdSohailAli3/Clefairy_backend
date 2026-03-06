from app.db.mongodb import MongoManager


async def add_emergency_contact(contact_data: dict):
    emergency_contacts_collection = MongoManager.get_collection("emergency_contacts")
    return await emergency_contacts_collection.insert_one(contact_data)

async def get_user_contacts(user_id: int):
    emergency_contacts_collection = MongoManager.get_collection("emergency_contacts")

    contacts = []
    cursor = emergency_contacts_collection.find({"user_id":user_id})
    async for doc in cursor:
        contacts.append(doc)
    return list(contacts)
