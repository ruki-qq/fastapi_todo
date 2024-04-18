from api_v1.notes.schemas import Note, NoteCreate, NoteUpdate
from api_v1.tasks.schemas import Task, TaskCreate, TaskUpdate

type ApiItem = Note | Task
type ApiCreate = NoteCreate | TaskCreate
type ApiUpdate = NoteUpdate | TaskUpdate
