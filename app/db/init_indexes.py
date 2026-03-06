from app.db.mongodb import MongoManager


async def create_indexes():

    db = MongoManager.get_db()

    # posts feed optimization
    await db.posts.create_index("created_at")

    # comments lookup
    await db.comments.create_index("post_id")

    # prevent duplicate likes
    await db.likes.create_index(
        [("post_id", 1), ("user_id", 1)],
        unique=True
    )

    print("✅ MongoDB indexes ensured")