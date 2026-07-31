from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Investment Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_investment():
    user = create_test_user()

    investment = {
        "name": "Nifty Index Fund",
        "investment_type": "Mutual Fund",
        "amount": 10000,
        "current_value": 10500,
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/investments/",
        json=investment,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Nifty Index Fund"


def test_get_investments():
    response = client.get("/api/v1/investments/")

    assert response.status_code == 200


def test_get_investment_not_found():
    response = client.get("/api/v1/investments/999999")

    assert response.status_code == 404


def test_delete_investment():
    user = create_test_user()

    investment = {
        "name": "Gold ETF",
        "investment_type": "ETF",
        "amount": 5000,
        "current_value": 5200,
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/investments/",
        json=investment,
    )

    investment_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/investments/{investment_id}"
    )

    assert response.status_code == 200
