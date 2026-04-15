from fastapi import APIRouter, HTTPException, Query
from fb_apify.services.profile import ( get_facebook_profile, get_facebook_profile_id, get_all_facebook_posts)

profile_router = APIRouter()


@profile_router.get("/profile")
def fetch_facebook_profile(
    url: str = Query(..., description="Facebook profile/page URL"),
    include_posts: bool = False,
    max_posts: int = 5
):
    return get_facebook_profile(
        url=url,
        include_posts=include_posts,
        max_posts=max_posts
    )


@profile_router.get("/get_profile_id")
def fetch_facebook_profile_id(url: str):
    facebook_id = get_facebook_profile_id(url)

    if not facebook_id:
        raise HTTPException(status_code=404, detail="facebookId not found")

    return {
        "facebookId": facebook_id
    }


@profile_router.get("/posts/all")
def fetch_all_posts(url: str, resultsLimit: int):
    try: 
        return get_all_facebook_posts(url=url, resultsLimit=resultsLimit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))