from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_filter_transactions():
    response = client.get(
        "/api/v1/filters/transactions",
        params={"transaction_type": "expense"},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_transactions_by_wallet():
    response = client.get(
        "/api/v1/filters/transactions",
        params={"wallet_id": 1},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_transactions_by_category():
    response = client.get(
        "/api/v1/filters/transactions",
        params={"category_id": 1},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_transactions_no_filters():
    response = client.get("/api/v1/filters/transactions")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
