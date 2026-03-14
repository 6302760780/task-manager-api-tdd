from fastapi import APIRouter, HTTPException, Response, status
from app.models import TaskCreate
from app import store

router = APIRouter()


@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": store.next_id,
        "title": task.title,
        "completed": False
    }
    store.tasks.append(new_task)
    store.next_id += 1
    return new_task


@router.get("/tasks")
def get_tasks():
    return store.tasks


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for task in store.tasks:
        if task["id"] == task_id:
            store.tasks.remove(task)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail="Task not found")