from fastapi import APIRouter, HTTPException, Query
from fb_apify.services.profile import get_facebook_profile

profile_router = APIRouter()


@profile_router.get("/profile")
def fetch_facebook_profile(
    url: str = Query(..., description="Facebook profile/page URL"),
    include_posts: bool = False,
    max_posts: int = 5
):
    data = get_facebook_profile(
        url=url,
        include_posts=include_posts,
        max_posts=max_posts
    )

    if not data:
        raise HTTPException(status_code=404, detail="Profile not found")

    return {
        "status": "success",
        "data": data
    }