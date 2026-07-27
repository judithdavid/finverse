from uuid import uuid4

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
    email = f"{uuid4()}@example.com"

    response = client.post(
        "/api/v1/users/",
        json={
            "email": email,
            "full_name": "Test User",
            "password": "password123",
        },
    )

    assert response.status_code == 201


def test_create_duplicate_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Test User",
        "password": "password123",
    }

    first_response = client.post("/api/v1/users/", json=user)
    assert first_response.status_code == 201

    second_response = client.post("/api/v1/users/", json=user)
    assert second_response.status_code == 409


def test_get_user():
    response = client.get("/api/v1/users/1")

    assert response.status_code in [200, 404]


def test_create_user_invalid_email():
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "invalid-email",
            "full_name": "Test User",
            "password": "password123",
        },
    )

    assert response.status_code == 422

def test_login():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Login Test",
        "password": "password123",
    }

    create_response = client.post("/api/v1/users/", json=user)
    assert create_response.status_code == 201

    login_response = client.post(
        "/api/v1/users/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_get_current_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Protected User",
        "password": "password123",
    }

    create_response = client.post("/api/v1/users/", json=user)
    assert create_response.status_code == 201

    login_response = client.post(
        "/api/v1/users/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/api/v1/users/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200
    assert response.json()["email"] == email

def test_login_invalid_password():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Invalid Login",
        "password": "password123",
    }

    create_response = client.post("/api/v1/users/", json=user)
    assert create_response.status_code == 201

    login_response = client.post(
        "/api/v1/users/login",
        json={
            "email": email,
            "password": "wrongpassword",
        },
    )

    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Invalid email or password"
