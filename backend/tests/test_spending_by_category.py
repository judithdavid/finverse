from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_spending_by_category():
    response = client.get(
        "/api/v1/analytics/spending-by-category"
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_spending_by_category_response():
    response = client.get(
        "/api/v1/analytics/spending-by-category"
    )

    assert response.status_code == 200

    data = response.json()

    if data:
        assert "category" in data[0]
        assert "total_amount" in data[0]
