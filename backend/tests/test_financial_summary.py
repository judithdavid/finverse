from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_financial_summary():
    response = client.get("/api/v1/analytics/financial-summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_assets" in data
    assert "total_liabilities" in data
    assert "net_worth" in data
    assert "savings_rate" in data


def test_financial_summary_response_types():
    response = client.get("/api/v1/analytics/financial-summary")

    data = response.json()

    assert isinstance(data["total_assets"], (int, float))
    assert isinstance(data["total_liabilities"], (int, float))
    assert isinstance(data["net_worth"], (int, float))
    assert isinstance(data["savings_rate"], (int, float))