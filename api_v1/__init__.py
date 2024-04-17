from fastapi import APIRouter

from .notes.views import router as router_notes

router_v1 = APIRouter()
router_v1.include_router(router_notes, prefix="/notes")