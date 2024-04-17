from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict

from api_v1.mixins import NoteTaskSchemaMixin


class TaskBase(NoteTaskSchemaMixin, BaseModel):
    pass


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: Annotated[str, MinLen(1), MaxLen(50)] | None = None
    text: str | None = None
    in_process: bool | None = None
    finished: bool | None = None


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
