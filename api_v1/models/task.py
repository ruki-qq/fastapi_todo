from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.mixins import NoteTaskModelMixin
from core.models import Base, UserRelationMixin


class Task(UserRelationMixin, NoteTaskModelMixin, Base):
    _user_back_populates = "tasks"

    in_process: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="True"
    )
    finished: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="False"
    )
