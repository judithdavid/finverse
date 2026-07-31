from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_report():
    response = client.get("/api/v1/reports/")

    assert response.status_code == 200

    data = response.json()

    assert "total_income" in data
    assert "total_expense" in data
    assert "total_balance" in data
    assert "total_budget" in data
    assert "total_savings" in data
    assert "total_investments" in data
    assert "total_loans" in data
