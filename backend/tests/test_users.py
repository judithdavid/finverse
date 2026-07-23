from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200


def test_get_users():
    response = client.get("/api/v1/users/")

    assert response.status_code == 200


def test_create_user():
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "full_name": "Test User",
            "password": "password123",
        },
    )

    assert response.status_code == 201


def test_get_user():
    response = client.get("/api/v1/users/1")

    assert response.status_code in [200, 404]
