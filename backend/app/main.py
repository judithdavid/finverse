from fastapi import FastAPI
from backend.app.core.config import APP_NAME, APP_VERSION
from backend.app.api.v1.router import router
# from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from backend.app.core.rate_limit import limiter

from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.cors import CORS_SETTINGS

from backend.app.core.exceptions import (
    register_exception_handlers,
)



app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)
register_exception_handlers(app)

app.include_router(router, prefix="/api/v1", tags=["API"])
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    **CORS_SETTINGS,
)



@app.get("/")
def root():
    return {"message": f"Welcome to {APP_NAME}"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}