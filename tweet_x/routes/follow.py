from fastapi import APIRouter, HTTPException
from tweet_x.services.follow import (
    get_followers,
    get_following,
    search_followers
)

follow_router = APIRouter()


@follow_router.get("/{user_id}/followers")
def followers(user_id: str, pagination_token: str = None):
    try:
        return get_followers(user_id, pagination_token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@follow_router.get("/{user_id}/following")
def following(user_id: str, pagination_token: str = None):
    try:
        return get_following(user_id, pagination_token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@follow_router.get("/{user_id}/followers/search")
def search_in_followers(user_id: str, keyword: str):
    try:
        return search_followers(user_id, keyword)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))