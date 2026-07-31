from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Bill Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_bill():
    user = create_test_user()

    bill = {
        "name": "Electricity Bill",
        "amount": 1500,
        "due_date": "2026-08-10",
        "is_paid": False,
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/bills/",
        json=bill,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Electricity Bill"


def test_get_bills():
    response = client.get("/api/v1/bills/")

    assert response.status_code == 200


def test_get_bill_not_found():
    response = client.get("/api/v1/bills/999999")

    assert response.status_code == 404


def test_delete_bill():
    user = create_test_user()

    bill = {
        "name": "Internet Bill",
        "amount": 999,
        "due_date": "2026-08-15",
        "is_paid": False,
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/bills/",
        json=bill,
    )

    bill_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/bills/{bill_id}"
    )

    assert response.status_code == 200