from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_rate_limit_create_user():
    status_codes = []

    for _ in range(11):
        response = client.post(
            "/api/v1/users/",
            json={
                "email": f"{uuid4()}@example.com",
                "full_name": "Rate Limit User",
                "password": "password123",
            },
        )

        status_codes.append(response.status_code)

    assert 429 in status_codes