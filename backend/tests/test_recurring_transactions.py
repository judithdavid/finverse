from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_wallet_and_category():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Recurring Transaction Test User",
        "password": "password123",
    }

    user_response = client.post("/api/v1/users/", json=user)
    user_id = user_response.json()["id"]

    wallet = {
        "name": "Primary Wallet",
        "balance": 10000,
        "user_id": user_id,
    }

    wallet_response = client.post(
        "/api/v1/wallets/",
        json=wallet,
    )

    category = {
        "name": "Salary",
        "category_type": "income",
        "user_id": user_id,
    }

    category_response = client.post(
        "/api/v1/categories/",
        json=category,
    )

    return {
        "wallet_id": wallet_response.json()["id"],
        "category_id": category_response.json()["id"],
    }


def test_create_recurring_transaction():
    data = create_test_wallet_and_category()

    recurring_transaction = {
        "description": "Monthly Salary",
        "amount": 50000,
        "transaction_type": "income",
        "frequency": "monthly",
        "wallet_id": data["wallet_id"],
        "category_id": data["category_id"],
    }

    response = client.post(
        "/api/v1/recurring-transactions/",
        json=recurring_transaction,
    )

    assert response.status_code == 201
    assert response.json()["description"] == "Monthly Salary"


def test_get_recurring_transactions():
    response = client.get("/api/v1/recurring-transactions/")

    assert response.status_code == 200


def test_get_recurring_transaction_not_found():
    response = client.get("/api/v1/recurring-transactions/999999")

    assert response.status_code == 404


def test_delete_recurring_transaction():
    data = create_test_wallet_and_category()

    recurring_transaction = {
        "description": "Netflix",
        "amount": 649,
        "transaction_type": "expense",
        "frequency": "monthly",
        "wallet_id": data["wallet_id"],
        "category_id": data["category_id"],
    }

    created = client.post(
        "/api/v1/recurring-transactions/",
        json=recurring_transaction,
    )

    recurring_transaction_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/recurring-transactions/{recurring_transaction_id}"
    )

    assert response.status_code == 200
