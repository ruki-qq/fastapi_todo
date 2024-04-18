from api_v1.utils import BaseObjectCRUD, BaseObjectDependencies
from api_v1.models import Note


note_crud = BaseObjectCRUD(Note)
note_dependencies = BaseObjectDependencies(note_crud, "note")
