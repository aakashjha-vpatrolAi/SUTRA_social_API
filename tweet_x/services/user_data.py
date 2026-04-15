from tweet_x.functions.core import make_request
from tweet_x.x_config import x_config


def get_user_profile(username: str):
    url = f"{x_config.X_BASE_URL}/users/by/username/{username}"
    return make_request(url)


def search_users(query: str, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/users/search"

    params = {
        "query": query,
        "max_results": max_results,
        "user.fields": "id,name,username,description,public_metrics"
    }
    return make_request(url, params)

def get_user_follow_counts(username: str):
    data = get_user_profile(username)

    user = data.get("data", {})
    metrics = user.get("public_metrics", {})

    return {
        "user_id": user.get("id"),
        "username": user.get("username"),
        "followers_count": metrics.get("followers_count", 0),
        "following_count": metrics.get("following_count", 0)
    }
