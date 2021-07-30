from app.main import app
from fastapi.testclient import TestClient


def test_create_author(temp_db):
    request_data = {
        "name": "Wilson"
    }
    with TestClient(app) as client:
        # Create author
        response = client.post("/authors/create", json=request_data)
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Wilson"


def test_authors_detail(temp_db):
    author_id = 1
    with TestClient(app) as client:
        response = client.get(f"/authors/get/{author_id}")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Wilson"


def test_authors_list(temp_db):
    with TestClient(app) as client:
        response = client.get("/authors/get_all")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["name"] == "Wilson"


def test_update_author(temp_db):
    author_id = 1
    request_data = {
        "name": "Smith"
    }
    with TestClient(app) as client:
        response = client.put(f"/authors/{author_id}", json=request_data)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Smith"