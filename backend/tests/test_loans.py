
from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Loan Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_loan():
    user = create_test_user()

    loan = {
        "lender": "ABC Bank",
        "amount": 500000,
        "remaining_amount": 450000,
        "interest_rate": 8.5,
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/loans/",
        json=loan,
    )

    assert response.status_code == 201
    assert response.json()["lender"] == "ABC Bank"


def test_get_loans():
    response = client.get("/api/v1/loans/")

    assert response.status_code == 200


def test_get_loan_not_found():
    response = client.get("/api/v1/loans/999999")

    assert response.status_code == 404


def test_delete_loan():
    user = create_test_user()

    loan = {
        "lender": "XYZ Finance",
        "amount": 100000,
        "remaining_amount": 90000,
        "interest_rate": 10.0,
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/loans/",
        json=loan,
    )

    loan_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/loans/{loan_id}"
    )

    assert response.status_code == 200
