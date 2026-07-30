from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Category Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_category():
    user = create_test_user()

    category = {
        "name": "Food",
        "category_type": "expense",
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/categories/",
        json=category,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Food"


def test_get_categories():
    response = client.get("/api/v1/categories/")

    assert response.status_code == 200


def test_get_category_not_found():
    response = client.get("/api/v1/categories/999999")

    assert response.status_code == 404


def test_delete_category():
    user = create_test_user()

    category = {
        "name": "Shopping",
        "category_type": "expense",
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/categories/",
        json=category,
    )

    category_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/categories/{category_id}"
    )

    assert response.status_code == 200
