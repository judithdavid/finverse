
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_monthly_report():
    response = client.get("/api/v1/analytics/monthly-report")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_monthly_report_response():
    response = client.get("/api/v1/analytics/monthly-report")

    assert response.status_code == 200

    data = response.json()

    if data:
        assert "month" in data[0]
        assert "income" in data[0]
        assert "expense" in data[0]
