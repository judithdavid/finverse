from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_category():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Budget Test User",
        "password": "password123",
    }

    user_response = client.post("/api/v1/users/", json=user)
    user_id = user_response.json()["id"]

    category = {
        "name": "Food",
        "category_type": "expense",
        "user_id": user_id,
    }

    category_response = client.post(
        "/api/v1/categories/",
        json=category,
    )

    return {
        "user_id": user_id,
        "category_id": category_response.json()["id"],
    }


def test_create_budget():
    data = create_test_category()

    budget = {
        "amount": 5000,
        "category_id": data["category_id"],
        "user_id": data["user_id"],
    }

    response = client.post(
        "/api/v1/budgets/",
        json=budget,
    )

    assert response.status_code == 201
    assert response.json()["amount"] == 5000


def test_get_budgets():
    response = client.get("/api/v1/budgets/")

    assert response.status_code == 200


def test_get_budget_not_found():
    response = client.get("/api/v1/budgets/999999")

    assert response.status_code == 404


def test_delete_budget():
    data = create_test_category()

    budget = {
        "amount": 2000,
        "category_id": data["category_id"],
        "user_id": data["user_id"],
    }

    created = client.post(
        "/api/v1/budgets/",
        json=budget,
    )

    budget_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/budgets/{budget_id}"
    )

    assert response.status_code == 200