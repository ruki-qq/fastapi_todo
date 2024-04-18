from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.models import Note, Task
from api_v1.notes.schemas import NoteCreate, NoteUpdate
from api_v1.tasks.schemas import TaskCreate, TaskUpdate


async def get_objects(
    session: AsyncSession, obj_model: Type[Note | Task]
) -> list[Note | Task]:
    objs = await session.scalars(
        select(obj_model).order_by(obj_model.created_at.desc(), obj_model.id)
    )
    return list(objs)


async def get_object(
    session: AsyncSession, obj_model: Type[Note | Task], obj_id: int
) -> Note | Task | None:
    return await session.get(obj_model, obj_id)


async def create_object(
    session: AsyncSession, obj_model: Type[Note | Task], obj_in: NoteCreate | TaskCreate
) -> Note | Task:
    obj = obj_model(**obj_in.model_dump())
    session.add(obj)
    await session.commit()
    return obj


async def update_object(
    session: AsyncSession, obj: Note | Task, obj_update: NoteUpdate | TaskUpdate
) -> Note | Task:
    for name, val in obj_update.model_dump(exclude_unset=True).items():
        setattr(obj, name, val)
    await session.commit()
    return obj


async def delete_object(session: AsyncSession, obj: Note | Task) -> None:
    await session.delete(obj)
    await session.commit()
