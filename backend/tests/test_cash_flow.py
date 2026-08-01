from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_cash_flow():
    response = client.get("/api/v1/analytics/cash-flow")

    assert response.status_code == 200

    data = response.json()

    assert "total_income" in data
    assert "total_expense" in data
    assert "net_cash_flow" in data


def test_cash_flow_response_types():
    response = client.get("/api/v1/analytics/cash-flow")

    data = response.json()

    assert isinstance(data["total_income"], (int, float))
    assert isinstance(data["total_expense"], (int, float))
    assert isinstance(data["net_cash_flow"], (int, float))