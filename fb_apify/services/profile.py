from fb_apify.functions.core import run_actor
from fb_apify.fb_apify_config import apify_settings


def get_facebook_profile(url: str, include_posts: bool = False, max_posts: int = None):
    run_input = {
        "startUrls": [{"url": url}],
        "resultsLimit": apify_settings.DEFAULT_RESULTS_LIMIT,
    }

    if include_posts:
        run_input["includePosts"] = True
        run_input["maxPosts"] = max_posts or apify_settings.DEFAULT_MAX_POSTS

    results = run_actor(
        actor_id=apify_settings.FACEBOOK_PAGE_ACTOR,
        run_input=run_input
    )

    if not results:
        return None

    return results[0]