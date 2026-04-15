from fastapi import APIRouter
from .profile import profile_router

router = APIRouter()

# router.include_router(user_router, prefix="/users")#, tags=["FB Users"])
# router.include_router(post_router, prefix="/posts")#, tags=["FB Posts"])
router.include_router(profile_router, prefix="/profile")#, tags=["FB-Apify Profile"])

