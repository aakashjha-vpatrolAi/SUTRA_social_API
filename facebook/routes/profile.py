from fastapi import APIRouter, HTTPException
from facebook.services.profile import get_profile_details, get_page_details, get_profile_id

profile_router = APIRouter()


@profile_router.get("/details")
def profile_details(profile_url: str):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_cd7a94c1-5880-434f-8119-121c1589a464"""
    try:
        return get_profile_details(profile_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@profile_router.get("/page/details")
def page_details(page_url: str):
    """ https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_847dc586-dd05-4660-a838-128c872a1407
    
    followers_count, following_count, post_count, categories, is_verified"""
    try:
        return get_page_details(page_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@profile_router.get("/get-profile-id")
def get_user_profile_id(profile_url: str):
    """https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_e8f05277-cc6d-4e96-bd1d-725c861eb9e4"""
    try:
        return get_profile_id(profile_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))