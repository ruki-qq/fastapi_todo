from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from api_v1.models import Note, Task


class User(Base):
    username: Mapped[str] = mapped_column(String(16), unique=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    register_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )

    first_name: Mapped[str | None] = mapped_column(String(64))
    last_name: Mapped[str | None] = mapped_column(String(64))
    bio: Mapped[str | None] = mapped_column(Text)
    notes: Mapped[list["Note"]] = relationship(back_populates="user")
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} username={self.username}"

    def __repr__(self):
        return str(self)
