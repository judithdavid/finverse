from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_wallet():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Transaction Test User",
        "password": "password123",
    }

    user_response = client.post("/api/v1/users/", json=user)
    user_id = user_response.json()["id"]

    wallet = {
        "name": "Primary Wallet",
        "balance": 1000,
        "user_id": user_id,
    }

    wallet_response = client.post("/api/v1/wallets/", json=wallet)

    return wallet_response.json()


def test_create_transaction():
    wallet = create_test_wallet()

    transaction = {
        "amount": 250,
        "description": "Groceries",
        "transaction_type": "expense",
        "wallet_id": wallet["id"],
    }

    response = client.post(
        "/api/v1/transactions/",
        json=transaction,
    )

    assert response.status_code == 201
    assert response.json()["description"] == "Groceries"


def test_get_transactions():
    response = client.get("/api/v1/transactions/")

    assert response.status_code == 200


def test_get_transaction_not_found():
    response = client.get("/api/v1/transactions/999999")

    assert response.status_code == 404


def test_delete_transaction():
    wallet = create_test_wallet()

    transaction = {
        "amount": 100,
        "description": "Coffee",
        "transaction_type": "expense",
        "wallet_id": wallet["id"],
    }

    created = client.post(
        "/api/v1/transactions/",
        json=transaction,
    )

    transaction_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/transactions/{transaction_id}"
    )

    assert response.status_code == 200
