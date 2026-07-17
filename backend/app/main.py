from fastapi import FastAPI
from backend.app.core.config import APP_NAME, APP_VERSION
from backend.app.api.v1.router import router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

app.include_router(router, prefix="/api/v1", tags=["API"])


@app.get("/")
def root():
    return {"message": f"Welcome to {APP_NAME}"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}