from tweet_x.x_config import x_config
from tweet_x.functions.core import make_request


def get_followers(user_id: str, pagination_token: str = None, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/users/{user_id}/followers"

    params = {
        "max_results": max_results,
        "user.fields": "id,name,username,public_metrics"
    }

    if pagination_token:
        params["pagination_token"] = pagination_token

    return make_request(url, params=params)


def get_following(user_id: str, pagination_token: str = None, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/users/{user_id}/following"

    params = {
        "max_results": max_results,
        "user.fields": "id,name,username,public_metrics"
    }

    if pagination_token:
        params["pagination_token"] = pagination_token

    return make_request(url, params=params)


def search_followers(user_id: str, keyword: str):
    data = get_followers(user_id)

    users = data.get("data", [])

    keyword = keyword.lower()

    return [
        u for u in users
        if keyword in (u.get("username", "").lower())
        or keyword in (u.get("name", "").lower())
    ]