from api_v1.mixins import NoteTaskModelMixin
from core.models import Base, UserRelationMixin


class Note(UserRelationMixin, NoteTaskModelMixin, Base):
    _user_back_populates = "notes"
