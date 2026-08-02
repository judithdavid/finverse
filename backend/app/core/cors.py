ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8501",
]

CORS_SETTINGS = {
    "allow_origins": ALLOWED_ORIGINS,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
