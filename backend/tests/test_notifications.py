from uuid import uuid4

from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def create_test_user():
    email = f"{uuid4()}@example.com"

    user = {
        "email": email,
        "full_name": "Notification Test User",
        "password": "password123",
    }

    response = client.post("/api/v1/users/", json=user)

    return response.json()


def test_create_notification():
    user = create_test_user()

    notification = {
        "title": "Budget Alert",
        "message": "You have exceeded your monthly budget.",
        "is_read": False,
        "user_id": user["id"],
    }

    response = client.post(
        "/api/v1/notifications/",
        json=notification,
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Budget Alert"


def test_get_notifications():
    response = client.get("/api/v1/notifications/")

    assert response.status_code == 200


def test_get_notification_not_found():
    response = client.get("/api/v1/notifications/999999")

    assert response.status_code == 404


def test_delete_notification():
    user = create_test_user()

    notification = {
        "title": "Bill Reminder",
        "message": "Electricity bill is due tomorrow.",
        "is_read": False,
        "user_id": user["id"],
    }

    created = client.post(
        "/api/v1/notifications/",
        json=notification,
    )

    notification_id = created.json()["id"]

    response = client.delete(
        f"/api/v1/notifications/{notification_id}"
    )

    assert response.status_code == 200
