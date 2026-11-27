from fastapi import APIRouter, HTTPException

from app.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

# In-memory storage: replaced by a database in a later session
_tasks: dict[int, Task] = {}
_next_id = 1


def reset_storage() -> None:
    """Empty the store (used by tests)."""
    global _next_id
    _tasks.clear()
    _next_id = 1


def _get_or_404(task_id: int) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=Task, status_code=201)
def create_task(payload: TaskCreate) -> Task:
    global _next_id
    task = Task(id=_next_id, **payload.model_dump())
    _tasks[task.id] = task
    _next_id += 1
    return task


@router.get("", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(_tasks.values())


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    return _get_or_404(task_id)