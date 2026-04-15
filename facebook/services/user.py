from typing import Optional
from facebook.fb_config import fb_config
from facebook.functions.core import make_request


def get_search_people(query: str, cursor: Optional[str] = None):
    url = f"{fb_config.FB_BASE_URL}/search/people" 

    params = {
        "query": query,
        "cursor": cursor
    }

    return make_request(url, method="GET", params=params)