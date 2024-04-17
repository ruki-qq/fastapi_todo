from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict

from api_v1.mixins import NoteTaskSchemaMixin


class NoteBase(NoteTaskSchemaMixin, BaseModel):
    pass


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title: Annotated[str, MinLen(1), MaxLen(50)] | None = None
    text: str | None = None


class Note(NoteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
