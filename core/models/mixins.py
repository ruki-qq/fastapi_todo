from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from users.models import User


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(self) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.id"),
            nullable=self._user_id_nullable,
            unique=self._user_id_unique,
        )

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship(back_populates=self._user_back_populates)


class NoteTaskMixin:
    title: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text, default="", server_default="")

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} title={self.title}"

    def __repr__(self):
        return str(self)
