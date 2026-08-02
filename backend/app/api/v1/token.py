from fastapi import APIRouter, HTTPException

from backend.app.schemas.token import (
    RefreshTokenRequest,
    TokenResponse,
)
from backend.app.services.token_service import TokenService

router = APIRouter(
    prefix="/token",
    tags=["Authentication"],
)


@router.post(
    "/refresh",
    response_model=TokenResponse,
)
def refresh_token(
    request: RefreshTokenRequest,
):
    service = TokenService()

    token = service.refresh_access_token(
        request.refresh_token
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token",
        )

    return token
