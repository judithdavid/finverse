from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_refresh_token():
    response = client.post(
        "/api/v1/token/refresh",
        json={
            "refresh_token": "dummy-refresh-token",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_refresh_token_invalid():
    response = client.post(
        "/api/v1/token/refresh",
        json={
            "refresh_token": "",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid refresh token"
