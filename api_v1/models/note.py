from api_v1.mixins import NoteTaskModelMixin
from core.models import Base


class Note(NoteTaskModelMixin, Base):
    pass
