from fastapi import APIRouter

from .user_data import user_router
from .tweets import tweet_router
from .follow import follow_router

tweet_x_router = APIRouter()

tweet_x_router.include_router(user_router, prefix="/users", tags=["Users"])
tweet_x_router.include_router(tweet_router, prefix="/tweets", tags=["Tweets"])
tweet_x_router.include_router(follow_router, prefix="/follow", tags=["Follow"])
