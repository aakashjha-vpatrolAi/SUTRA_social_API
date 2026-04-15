from facebook.fb_config import fb_config
from facebook.functions.core import make_request


def get_profile_details(profile_url: str):
    url = f"{fb_config.FB_BASE_URL}/profile/details_url"

    params = {
        "url": profile_url
    }

    return make_request(url, method="GET", params=params)

def get_page_details(page_url: str):
    url = f"{fb_config.FB_BASE_URL}/page/details"

    params = {
        "url": page_url
    }

    return make_request(url, method="GET", params=params)

def get_profile_id(profile_url: str):
    url = f"{fb_config.FB_BASE_URL}/profile/profile_id"

    params = {
        "url": profile_url
    }

    return make_request(url, method="GET", params=params)