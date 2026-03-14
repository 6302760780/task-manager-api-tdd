from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task_returns_201():
    response = client.post("/tasks", json={"title": "Learn TDD"})
    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Learn TDD"
    assert data["completed"] is False