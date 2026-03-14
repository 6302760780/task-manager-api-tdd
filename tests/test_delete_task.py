from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_delete_task_removes_task():
    created = client.post("/tasks", json={"title": "Delete me"})
    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    all_tasks = client.get("/tasks").json()
    assert all_tasks == []