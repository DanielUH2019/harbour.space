"""Problem 06: POST -> GET tasks flow.

Task:
1. Keep in-memory task storage (dict or list)
2. Implement POST /tasks to add task with generated id
3. Implement GET /tasks to return all tasks
4. Verify: after POST, GET returns added task

Optional:
- Add GET /tasks/{task_id} with 404 for missing task
"""

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskIn(BaseModel):
    # TODO: add fields
    title: str
    completed: bool = False


class TaskOut(TaskIn):
    # TODO: add id + task fields
    id: int


# TODO: create in-memory storage and next_id counter
storage = {}
next_id = 0


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> TaskOut:
    # TODO: create/store/return task
    global next_id
    task = TaskOut(**payload.model_dump(), id=next_id)
    storage[next_id] = task 
    next_id += 1
    return task

@app.get(f"/tasks/{id}")
def get_task(id: int):
    if id not in storage:
        raise HTTPException(status_code=404)
    return storage[id]

@app.get("/tasks", response_model=list[TaskOut])
def get_tasks() -> list[TaskOut]:
    # TODO: return all tasks
    return [t for _, t in storage.items()]



