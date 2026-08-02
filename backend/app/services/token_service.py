from backend.app.core.security import create_access_token


class TokenService:
    def refresh_access_token(
        self,
        refresh_token: str,
    ):
        # Placeholder validation.
        # Replace with real refresh token verification later.
        if not refresh_token:
            return None

        access_token = create_access_token(
            data={"sub": "user"}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
