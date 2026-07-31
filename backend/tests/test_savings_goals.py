
from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Savings Goal Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_savings_goal():
    user = create_test_user()

    savings_goal = {
        "name": "Emergency Fund",
        "target_amount": 50000,
        "current_amount": 10000,
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/savings-goals/",
        json=savings_goal,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Emergency Fund"


def test_get_savings_goals():
    response = client.get("/api/v1/savings-goals/")

    assert response.status_code == 200


def test_get_savings_goal_not_found():
    response = client.get("/api/v1/savings-goals/999999")

    assert response.status_code == 404


def test_delete_savings_goal():
    user = create_test_user()

    savings_goal = {
        "name": "Vacation",
        "target_amount": 20000,
        "current_amount": 5000,
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/savings-goals/",
        json=savings_goal,
    )

    savings_goal_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/savings-goals/{savings_goal_id}"
    )

    assert response.status_code == 200
