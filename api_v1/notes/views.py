from fastapi import APIRouter, status

router = APIRouter(tags=["notes"])


@router.get("")
async def get_notes():
    pass


@router.get("/{note_id}")
async def get_note_by_id(note_id: int):
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_note():
    pass


@router.patch("/{note_id}")
async def update_note(note_id: int):
    pass
