from datetime import datetime, timezone
# from app.db.mongodb import conversation_collection
from app.db.mongodb import MongoManager
from app.schemas.chat_schema import Message
from app.core.config import SYSTEM_PROMPT
from pymongo import ReturnDocument


async def get_or_create_conversation(user_id: int):
    conversation_collection = MongoManager.get_collection("conversations")
    conversation = await conversation_collection.find_one({"user_id": user_id})

    if not conversation:
        new_convo = {
            "user_id": user_id,
            "messages": [],
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }
        await conversation_collection.insert_one(new_convo)
        conversation = await conversation_collection.find_one({"user_id": user_id})

    return conversation


async def add_user_message(user_id: int, message: str):
    msg = Message(
        role="user",
        content=message+" My current location is: kookas Jaipur, Rajasthan, India.",
        timestamp=datetime.now(timezone.utc)
    )
    conversation_collection = MongoManager.get_collection("conversations")

    conversation = await conversation_collection.find_one_and_update(
        {"user_id": user_id},
        {
            "$push": {
                "messages": {
                    "$each": [msg.model_dump()],
                    "$slice": -100   # keep last 100 messages
                }
            },
            "$set": {"updated_at": datetime.now(timezone.utc)}
        },
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    return conversation
# It tells MongoDB:
# BEFORE → return document before update
# AFTER → return document after update

async def add_assistant_message(user_id: int, message: str):
    msg = Message(
        role="assistant",
        content=message,
        timestamp=datetime.now(timezone.utc)
    )
    conversation_collection = MongoManager.get_collection("conversations")

    await conversation_collection.update_one(
        {"user_id": user_id},
        {
            "$push": {
                "messages": {
                    "$each": [msg.model_dump()],
                    "$slice": -100
                }
            },
            "$set": {"updated_at": datetime.now(timezone.utc)}
        }
    )


async def format_for_llm_from_doc(conversation: dict):
    
    messages = conversation.get("messages", [])

    # limit history before sending to model
    messages = messages[-10:]

    formatted = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in messages
    ]

    # Inject system prompt dynamically
    formatted.insert(0, {
        "role": "system",
        "content": SYSTEM_PROMPT
    })

    return formatted
