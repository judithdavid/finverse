from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_transactions_pagination():
    response = client.get(
        "/api/v1/pagination/transactions",
        params={
            "page": 1,
            "page_size": 5,
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_sort_transactions_desc():
    response = client.get(
        "/api/v1/pagination/transactions",
        params={
            "sort_by": "amount",
            "order": "desc",
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_sort_transactions_asc():
    response = client.get(
        "/api/v1/pagination/transactions",
        params={
            "sort_by": "id",
            "order": "asc",
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
