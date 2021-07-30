import asyncio

from app.main import app
from app.schemas.authors import AuthorBase
from app.utils.authors import create_author
from fastapi.testclient import TestClient


def test_create_article(temp_db):
    author = AuthorBase(
        name="Wilson"
    )
    request_data = {
        "title": "What happens in spring?",
        "content": "Spring is a time when flowers bloom and trees begin to grow and reproduce.",
        "author_id": 1
    }
    with TestClient(app) as client:
        # Create author and add new article
        loop = asyncio.get_event_loop()
        author_db = loop.run_until_complete(create_author(author))
        response = client.post(
            "/articles/create", json=request_data)
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["title"] == "What happens in spring?"
    assert response.json()["content"] == "Spring is a time when flowers bloom and trees begin to grow and reproduce."
    assert response.json()["author_name"] == "Wilson"


def test_create_article_without_author(temp_db):
    request_data = {
        "title": "What happens in spring?",
        "content": "Spring is a time when flowers bloom and trees begin to grow and reproduce.",
        "author_id": 15
    }
    with TestClient(app) as client:
        response = client.post("/articles/create", json=request_data)
    assert response.status_code == 400


def test_articles_detail(temp_db):
    article_id = 1
    with TestClient(app) as client:
        response = client.get(f"/articles/get/{article_id}")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "What happens in spring?"
    assert response.json()["content"] == "Spring is a time when flowers bloom and trees begin to grow and reproduce."
    assert response.json()["author_name"] == "Wilson"


def test_articles_detail_by_author(temp_db):
    author_id = 1
    with TestClient(app) as client:
        response = client.get(f"/articles/get_by_author/{author_id}")
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1
    assert response.json()["results"][0]["title"] == "What happens in spring?"
    assert response.json()["results"][0]["content"] == "Spring is a time when flowers bloom and trees begin to grow and reproduce."
    assert response.json()["results"][0]["author_name"] == "Wilson"


def test_articles_list(temp_db):
    with TestClient(app) as client:
        response = client.get("/articles/get_all")
    assert response.status_code == 200
    assert response.json()["total_count"] == 1
    assert response.json()["results"][0]["id"] == 1
    assert response.json()["results"][0]["title"] == "What happens in spring?"
    assert response.json()["results"][0]["content"] == "Spring is a time when flowers bloom and trees begin to grow and reproduce."
    assert response.json()["results"][0]["author_name"] == "Wilson"


def test_update_article(temp_db):
    article_id = 1
    request_data = {
        "title": "When is the Spring season?",
        "content": "During Spring an important celebration takes place: Easter Day."
    }
    with TestClient(app) as client:
        response = client.put(f"/articles/{article_id}", json=request_data)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "When is the Spring season?"
    assert response.json()["content"] == "During Spring an important celebration takes place: Easter Day."
    assert response.json()["author_name"] == "Wilson"