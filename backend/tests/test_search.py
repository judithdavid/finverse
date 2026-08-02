from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_search_transactions():
    response = client.get(
        "/api/v1/search/transactions",
        params={"query": "Coffee"},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_empty_result():
    response = client.get(
        "/api/v1/search/transactions",
        params={"query": "this-does-not-exist"},
    )

    assert response.status_code == 200
    assert response.json() == []
