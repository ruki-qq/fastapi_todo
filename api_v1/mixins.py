from typing import Annotated

from annotated_types import MaxLen, MinLen
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class NoteTaskModelMixin:
    title: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text, default="", server_default="")

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} title={self.title}"

    def __repr__(self):
        return str(self)


class NoteTaskSchemaMixin:
    title: Annotated[str, MinLen(1), MaxLen(50)]
    text: str
