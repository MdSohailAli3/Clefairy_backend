# from pymongo import MongoClient
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)
from typing import Optional
# from pymongo.database import Database
# from pymongo.collection import Collection
import os
MONGO_URL = os.getenv("MONGO_URI")
DB_NAME = "women_safety"

class MongoManager:
    _client: Optional[AsyncIOMotorClient] = None
    _db: Optional[AsyncIOMotorDatabase] = None
    
    @classmethod
    async def connect(cls):
        cls._client = AsyncIOMotorClient(
            MONGO_URL,
            serverSelectionTimeoutMS=2000
        )

        await cls._client.admin.command("ping")

        cls._db = cls._client[DB_NAME]

        print("✅ MongoDB connected")

    @classmethod
    async def close(cls):
        if cls._client:
            cls._client.close()
            print("❌ MongoDB disconnected")

    @classmethod
    def get_db(cls) -> AsyncIOMotorDatabase:
        """Guarantee client exists."""
        if cls._db is None:
            raise RuntimeError("MongoDB not connected")
        return cls._db

    @classmethod
    def get_collection(cls, name: str) -> AsyncIOMotorCollection:
        return cls.get_db()[name]
