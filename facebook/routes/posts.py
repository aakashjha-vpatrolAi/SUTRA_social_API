from fastapi import APIRouter, HTTPException
from facebook.services.posts import get_user_posts
from typing import Optional
from facebook.functions.core import parse_to_date
from datetime import date, timedelta

post_router = APIRouter()


@post_router.get("/user-posts")
def user_posts(profile_id: str, cursor: str = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_7817d09c-d8c9-4e47-bcd1-fe48b3abd699"""
    try:
        start_date_parsed = parse_to_date(start_date, "start_date") if start_date else (date.today() - timedelta(days=30))
        end_date_parsed = parse_to_date(end_date, "end_date") if end_date else date.today()
        
        if start_date_parsed is not None and end_date_parsed is not None and start_date_parsed > end_date_parsed:
            raise HTTPException(status_code=400, detail=f"start_date must be <= end_date (got {start_date_parsed.isoformat()} > {end_date_parsed.isoformat()})")
        
        return get_user_posts(profile_id, cursor=cursor, 
                            start_date=start_date_parsed.isoformat(),
                            end_date=end_date_parsed.isoformat())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))