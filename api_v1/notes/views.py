from fastapi import APIRouter

from api_v1.notes.crud import note_crud, note_dependencies
from api_v1.notes.schemas import Note
from api_v1.utils import generate_routes

router = APIRouter(tags=["notes"])

generate_routes(router, note_crud, note_dependencies, Note)
