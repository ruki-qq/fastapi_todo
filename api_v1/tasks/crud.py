from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import crud_helper
from api_v1.models import Task
from api_v1.tasks.schemas import TaskCreate, TaskUpdate


async def get_tasks(session: AsyncSession) -> list[Task]:
    return await crud_helper.get_objects(session, Task)


async def get_task(session: AsyncSession, task_id: int) -> Task | None:
    return await crud_helper.get_object(session, Task, task_id)


async def create_task(session: AsyncSession, task_in: TaskCreate) -> Task:
    return await crud_helper.create_object(session, Task, task_in)


async def update_task(
    session: AsyncSession, task: Task, task_update: TaskUpdate
) -> Task:
    return await crud_helper.update_object(session, task, task_update)


async def delete_task(session: AsyncSession, task: Task) -> None:
    await crud_helper.delete_object(session, task)
