from datetime import date
from typing import Optional
from facebook.fb_config import fb_config
from facebook.functions.core import make_request


def get_user_posts(profile_id: str, start_date: date, end_date: date, cursor: Optional[str] = None):
    url = f"{fb_config.FB_BASE_URL}/profile/posts"

    params = {
        "profile_id": profile_id,
        "start_date": start_date,
        "end_date": end_date,
        "cursor": cursor 
    }

    return make_request(url, method="GET", params=params)