from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task_with_empty_title_returns_422():
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 422