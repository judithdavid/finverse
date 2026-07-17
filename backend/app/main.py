from fastapi import FastAPI

app = FastAPI(
    title="FinVerse API",
    description="Production-grade Personal Finance Platform API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FinVerse API"
    }