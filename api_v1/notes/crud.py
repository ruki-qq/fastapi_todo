from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import crud_helper
from api_v1.models import Note
from api_v1.notes.schemas import NoteCreate, NoteUpdate


async def get_notes(session: AsyncSession) -> list[Note]:
    return await crud_helper.get_objects(session, Note)


async def get_note(session: AsyncSession, note_id: int) -> Note | None:
    return await crud_helper.get_object(session, Note, note_id)


async def create_note(session: AsyncSession, note_in: NoteCreate) -> Note:
    return await crud_helper.create_object(session, Note, note_in)


async def update_note(
    session: AsyncSession, note: Note, note_update: NoteUpdate
) -> Note:
    return await crud_helper.update_object(session, note, note_update)


async def delete_note(session: AsyncSession, note: Note) -> None:
    await crud_helper.delete_object(session, note)
