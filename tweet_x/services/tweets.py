from tweet_x.functions.core import make_request
from tweet_x.x_config import x_config

def search_recent_posts(query: str, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/tweets/search/recent"

    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,text,author_id,created_at"
    }
    return make_request(url, params)

# TODO: add pagination or etc
def search_all_posts(query: str, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/tweets/search/all"

    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,text,author_id,created_at"
    }
    return make_request(url, params)


def count_posts(query: str):
    url = f"{x_config.X_BASE_URL}/tweets/counts/all"

    params = {
        "query": query,
        "granularity": "day"
    }
    return make_request(url, params)

def search_recent_hashtag(tag: str, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/tweets/search/recent"

    query = f"#{tag}"

    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,text,author_id,created_at,public_metrics"
    }

    return make_request(url, method="GET", params=params)


def search_all_hashtag(tag: str, max_results: int = 10):
    url = f"{x_config.X_BASE_URL}/tweets/search/all"

    query = f"#{tag}"

    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "id,text,author_id,created_at,public_metrics"
    }

    return make_request(url, method="GET", params=params)   



def search_by_location(query: str, location: str, max_results: int = 10):
    full_query = f"{query} place:{location}"

    return search_recent_posts(full_query, max_results)
