from datetime import datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column


class NoteTaskModelMixin:
    title: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text, default="", server_default="")
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} title={self.title}"

    def __repr__(self):
        return str(self)


class NoteTaskSchemaMixin:
    title: Annotated[str, MinLen(1), MaxLen(50)]
    text: str
