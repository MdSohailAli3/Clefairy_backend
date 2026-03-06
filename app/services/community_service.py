from datetime import datetime, UTC
from bson import ObjectId
from app.db.mongodb import MongoManager
from fastapi import HTTPException
from app.services.media_service import upload_media
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
# ---------------- POSTS ----------------

async def create_post(user_id, content, media):

    posts = MongoManager.get_collection("posts")

    media_url = None
    media_type = None

    # ---------- CLOUDINARY UPLOAD ----------
    if media:
        upload_result = await upload_media(media)

        media_url = upload_result["url"]
        media_type = upload_result["resource_type"]

    doc = {
        "user_id": user_id,
        "content": content,
        "media_url": media_url,
        "media_type": media_type,
        "likes_count": 0,
        "comments_count": 0,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC)
    }

    result = await posts.insert_one(doc)

    return {"post_id": str(result.inserted_id)} # stored in frontend to view post updates, like,comment etc


async def get_feed(page: int, limit: int):

    posts = MongoManager.get_collection("posts")

    skip = (page - 1) * limit # page - 1,2,3 & limit ex - 10

    cursor = (
        posts.find()
        .sort("created_at", -1) # newest
        .skip(skip) # pagination
        .limit(limit) # page size
    )

    results = await cursor.to_list(length=limit) # now query executes and data is fetched

    feed = []

    for p in results:
        feed.append({
            "post_id": str(p["_id"]),
            "user_id": p["user_id"],
            
            # content can be none
            "content": p.get("content"), # return none if not exist
            "media_url": p.get("media_url"),
            "media_type": p.get("media_type"),

            "likes_count": p["likes_count"],
            "comments_count": p["comments_count"],
            "created_at": p["created_at"]
        })

    return {"posts": feed, "page": page, "limit": limit}

async def get_trendings(page: int, limit: int):
    
    posts = MongoManager.get_collection("posts")
    skip = (page - 1) * limit # page - 1,2,3 & limit ex - 10

    cursor = (
        posts.find()
        .sort("likes_count", -1) # desc
        .skip(skip) # pagination
        .limit(limit) # page size
    )

    results = await cursor.to_list(length=limit) # now query executes and data is fetched

    feed = []

    for p in results:
        feed.append({
            "post_id": str(p["_id"]),
            "user_id": p["user_id"],
            
            # content can be none
            "content": p.get("content"), # return none if not exist
            "media_url": p.get("media_url"),
            "media_type": p.get("media_type"),

            "likes_count": p["likes_count"],
            "comments_count": p["comments_count"],
            "created_at": p["created_at"]
        })

    return {"trending_posts": feed, "page": page, "limit": limit}


async def delete_post(post_id: str, user_id: int):

    posts = MongoManager.get_collection("posts")

    result = await posts.delete_one({
        "_id": ObjectId(post_id),
        "user_id": user_id
    })
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Post not found or not authorized"
        )

    return {"message": "Post deleted"}


# ---------------- LIKES ----------------

async def like_post(post_id: str, user_id: int):

    likes = MongoManager.get_collection("likes")
    posts = MongoManager.get_collection("posts")

    try:
        await likes.insert_one({
            "post_id": post_id,
            "user_id": user_id,
            "created_at": datetime.now(UTC)
        })

        # increment only if insert succeeds
        await posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"likes_count": 1}}
        )

        return {"message": "liked"}

    except DuplicateKeyError:
        # user already liked
        return {"message": "already liked"}


async def unlike_post(post_id: str, user_id: int):

    likes = MongoManager.get_collection("likes")
    posts = MongoManager.get_collection("posts")

    result = await likes.delete_one({
        "post_id": post_id,
        "user_id": user_id
    })

    # decrement only if like existed
    if result.deleted_count == 1:
        await posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"likes_count": -1}}
        )

    return {"message": "unliked"}

# ---------------- COMMENTS ----------------

async def add_comment(post_id: str, data):

    comments = MongoManager.get_collection("comments")
    posts = MongoManager.get_collection("posts")

    doc = {
        "post_id": post_id,
        "user_id": data.user_id,
        "text": data.text,
        "created_at": datetime.now(UTC)
    }

    result = await comments.insert_one(doc)

    await posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$inc": {"comments_count": 1}}
    )

    return {"comment_id": str(result.inserted_id)}


async def get_comments(post_id: str):

    comments = MongoManager.get_collection("comments")

    cursor = comments.find({"post_id": post_id}).sort("created_at", -1)

    results = await cursor.to_list(length=100)

    response = []

    for c in results:
        response.append({
            "comment_id": str(c["_id"]),
            "post_id": c["post_id"],
            "user_id": c["user_id"],
            "text": c["text"],
            "created_at": c["created_at"]
        })

    return response

async def delete_comment(comment_id: str, user_id: int):

    comments = MongoManager.get_collection("comments")
    posts = MongoManager.get_collection("posts")

    # ---------- STEP 1: find comment ----------
    comment = await comments.find_one({
        "_id": ObjectId(comment_id)
    })

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    # ---------- STEP 2: delete comment ----------
    result = await comments.delete_one({
        "_id": ObjectId(comment_id),
        "user_id": user_id
    })

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to delete this comment"
        )

    # ---------- STEP 3: decrement counter ----------
    await posts.update_one(
        {"_id": ObjectId(comment["post_id"])},
        {"$inc": {"comments_count": -1}}
    )

    return {"message": "comment deleted"}