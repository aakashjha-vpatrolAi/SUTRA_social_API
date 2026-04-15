from fastapi import APIRouter, HTTPException
from tweet_x.services.user_data import get_user_profile, search_users, get_user_follow_counts

user_router = APIRouter()

@user_router.get("/user/{username}")
def fetch_user(username: str):
    try:
        return get_user_profile(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/search/users")
def users(query: str):
    try:
        return search_users(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/{username}/counts")
def user_counts(username: str):
    try:
        return get_user_follow_counts(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
