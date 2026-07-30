from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Wallet Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_wallet():
    user = create_test_user()

    wallet = {
        "name": "Savings",
        "balance": 5000,
        "user_id": user["id"],
    }

    response = client.post("/api/v1/wallets/", json=wallet)

    assert response.status_code == 201
    assert response.json()["name"] == "Savings"


def test_get_wallets():
    response = client.get("/api/v1/wallets/")

    assert response.status_code == 200


def test_get_wallet_not_found():
    response = client.get("/api/v1/wallets/999999")

    assert response.status_code == 404


def test_delete_wallet():
    user = create_test_user()

    wallet = {
        "name": "Temporary",
        "balance": 100,
        "user_id": user["id"],
    }

    created = client.post("/api/v1/wallets/", json=wallet)

    wallet_id = created.json()["id"]

    response = client.delete(f"/api/v1/wallets/{wallet_id}")

    assert response.status_code == 200
