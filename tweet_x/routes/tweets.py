from fastapi import APIRouter, HTTPException
from tweet_x.services.tweets import (
    search_recent_posts,
    search_all_posts,
    count_posts,
    search_recent_hashtag,
    search_all_hashtag,
)


tweet_router = APIRouter()

@tweet_router.get("/search/recent-posts")
def recent_posts(query: str):
    try:
        return search_recent_posts(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@tweet_router.get("/search/all-posts")
def all_posts(query: str):
    try:
        return search_all_posts(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@tweet_router.get("/search/post-count")
def post_count(query: str):
    try:
        return count_posts(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@tweet_router.get("/hashtag/recent/{tag}")
def recent_hashtag(tag: str, max_results: int = 10):
    try:
        return search_recent_hashtag(tag, max_results)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@tweet_router.get("/hashtag/all/{tag}")
def all_hashtag(tag: str, max_results: int = 10):
    try:
        return search_all_hashtag(tag, max_results)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
