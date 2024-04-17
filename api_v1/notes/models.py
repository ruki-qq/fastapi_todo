from core.models import Base
from core.models.mixins import NoteTaskMixin


class Note(NoteTaskMixin, Base):
    pass
