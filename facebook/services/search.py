from facebook.fb_config import fb_config
from facebook.functions.core import make_request
from typing import Optional

def get_search_global(
    query: str,
    location_uid: Optional[str] = None,
    recent_posts: Optional[bool] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None,
):
    url = f"{fb_config.FB_BASE_URL}/search/global"
    
    params = {
        "query": query,
        "recent_posts": recent_posts,
        "location_uid": location_uid,
        "start_date": start_date,  # YYYY-MM-DD
        "end_date": end_date,
        "cursor": cursor
    }

    return make_request(url, method="GET", params=params)


def get_search_posts(
    query: str,
    location_uid: Optional[str] = None,
    recent_posts: Optional[bool] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None,
):
    url = f"{fb_config.FB_BASE_URL}/search/posts"

    params = {
        "query": query,
        "recent_posts": recent_posts,
        "location_uid": location_uid,
        "start_date": start_date,  # YYYY-MM-DD
        "end_date": end_date,  # YYYY-MM-DD
        "cursor": cursor,
    }

    return make_request(url, method="GET", params=params)


def get_search_pages(query: str, cursor: Optional[str] = None, location_uid: Optional[str] = None):
    url = f"{fb_config.FB_BASE_URL}/search/pages"

    params = {
        "query": query,
        "location_uid": location_uid,
        "cursor": cursor
    }

    return make_request(url, method="GET", params=params)
