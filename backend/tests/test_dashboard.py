from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_dashboard():
    response = client.get("/api/v1/dashboard/")

    assert response.status_code == 200

    data = response.json()

    assert "total_balance" in data
    assert "total_income" in data
    assert "total_expense" in data
    assert "total_budget" in data


def test_dashboard_response_types():
    response = client.get("/api/v1/dashboard/")

    data = response.json()

    assert isinstance(data["total_balance"], (int, float))
    assert isinstance(data["total_income"], (int, float))
    assert isinstance(data["total_expense"], (int, float))
    assert isinstance(data["total_budget"], (int, float))
