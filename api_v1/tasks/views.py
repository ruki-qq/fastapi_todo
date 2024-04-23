from fastapi import APIRouter

from api_v1.tasks.crud import task_crud, task_dependencies
from api_v1.tasks.schemas import Task, TaskCreate, TaskUpdate
from api_v1.utils import generate_routes

router = APIRouter(tags=["tasks"])

generate_routes(router, task_crud, task_dependencies, Task, TaskCreate, TaskUpdate)


@router.post("/{task_id}/complete")
async def complete_task(task_id: int):
    pass


@router.post("/{task_id}/delete")
async def delete_task(task_id: int):
    pass
