from datetime import date, timedelta
from typing import Optional
from fastapi import APIRouter, HTTPException
from facebook.functions.core import parse_to_date
from facebook.services.user import get_search_people
from facebook.services.search import (
    get_search_global,
    get_search_posts,
    get_search_pages
)

user_router = APIRouter()


@user_router.get("/search-people")
def search_people(query: str, cursor: Optional[str] = None):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_f7a472b6-2abf-4d48-99ba-7927def033a6"""
    try:
        return get_search_people(query, cursor=cursor)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/search-global")
def search_global(
    query: Optional[str] = None,
    recent_posts: Optional[bool] = None,
    location_uid: Optional[str] = None,
    # Accepts YYYY-MM-DD only
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None
):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_1aa60f06-698a-4376-8674-91173700d761"""
    try:

        if not query:
            raise HTTPException(status_code=400, detail="query is required")

        start = parse_to_date(start_date, "start_date") or (date.today() - timedelta(days=30))
        end = parse_to_date(end_date, "end_date") or date.today()

        if start > end:
            raise HTTPException(
                status_code=400,
                detail=f"start_date must be <= end_date (got {start.isoformat()} > {end.isoformat()})",
            )

        return get_search_global(
            query,
            location_uid=location_uid,
            recent_posts=recent_posts,
            start_date=start.isoformat(),
            end_date=end.isoformat(),
            cursor=cursor,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/search-posts")
def search_posts(
    query: Optional[str] = None,
    recent_posts: Optional[bool] = None,
    location_uid: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None
):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_c0fb83cf-8dae-4824-a0ee-a66b79b037fb"""
    try:
        if not query:
            raise HTTPException(status_code=400, detail="query is required")

        start = parse_to_date(start_date, "start_date") if start_date is not None else None
        end = parse_to_date(end_date, "end_date") if end_date is not None else None

        if start is not None and end is not None and start > end:
            raise HTTPException(
                status_code=400,
                detail=f"start_date must be <= end_date (got {start.isoformat()} > {end.isoformat()})",
            )

        return get_search_posts(
            query,
            recent_posts=recent_posts,
            location_uid=location_uid,
            start_date=start.isoformat() if start is not None else None,
            end_date=end.isoformat() if end is not None else None,
            cursor=cursor,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/search-pages")
def search_pages(query: str, cursor: Optional[str] = None, location_uid: Optional[str] = None):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_6fc14979-9524-4671-8742-0fc6e8824a2a"""
    try:
        return get_search_pages(query, cursor=cursor, location_uid=location_uid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
