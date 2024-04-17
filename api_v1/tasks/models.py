from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import NoteTaskMixin


class Task(NoteTaskMixin, Base):
    in_process: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="True"
    )
    finished: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="False"
    )
