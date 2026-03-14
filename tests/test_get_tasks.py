from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_tasks_returns_created_tasks():
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"