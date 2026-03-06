from fastapi import APIRouter, Query
from fastapi import UploadFile, File, Form
from app.schemas.community_schema import CommentCreate
from app.services import community_service

router = APIRouter(prefix="/community", tags=["Community"])


# -------- POSTS --------

from fastapi import UploadFile, File, Form


@router.post("/posts")
async def create_post(
    user_id: int = Form(...),
    content: str | None = Form(None),
    media: UploadFile | None = File(None)
):
    return await community_service.create_post(
        user_id,
        content,
        media
    )

@router.get("/feed")
async def get_feed(
    page: int = Query(1, ge=1), # request - > /feed?page=2&limit=20,
    limit: int = Query(10, le=50)  # ge- greater-equal, le- less-equal
):                                  # 1 and 10 are default values
    return await community_service.get_feed(page, limit)


@router.get("/feed/trending")
async def get_trending(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50)
):
    return await community_service.get_trendings(page, limit)

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str, user_id: int):
    return await community_service.delete_post(post_id, user_id)


# -------- LIKES --------

@router.post("/posts/{post_id}/like")
async def like_post(post_id: str, user_id: int):
    return await community_service.like_post(post_id, user_id)


@router.delete("/posts/{post_id}/like")
async def unlike_post(post_id: str, user_id: int):
    return await community_service.unlike_post(post_id, user_id)


# -------- COMMENTS --------

@router.post("/posts/{post_id}/comments")
async def add_comment(post_id: str, data: CommentCreate):
    return await community_service.add_comment(post_id, data)


@router.get("/posts/{post_id}/comments")
async def get_comments(post_id: str):
    return await community_service.get_comments(post_id)


@router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: str, user_id: int):
    return await community_service.delete_comment(comment_id, user_id)