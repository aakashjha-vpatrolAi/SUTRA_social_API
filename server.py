import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config
from logger import setupLogger

# Import routers
# from tweet_x.routes import tweet_x_router
from facebook.routes import router as fb_router
from fb_apify.routes import router as fb_apify_router


app = FastAPI(title="SURTA APIs")

logger = setupLogger(__name__)

allowedOrigins = ["*"] if config.DEV_MODE else config.CORS_ALLOWED_ORIGIN

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowedOrigins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "SURTA APIs root endpoint. Please refer to the documentation for available endpoints."}


# Include routers
# app.include_router(tweet_x_router, prefix="/tweet-x", tags=["Tweet X"])

app.include_router(fb_router, prefix="/facebook", tags=["FB APIs"])
app.include_router(fb_apify_router, prefix="/facebook/apify", tags=["FB-appify APIs"])


# if __name__ == "__main__":
#     logger.info("Starting SURTA APIs server...")
#     uvicorn.run("server:app", host=config.HOST, port=config.SERVER_PORT, reload=True)
#     uvicorn.run("server:app", reload=True)

    