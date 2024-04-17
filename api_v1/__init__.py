from fastapi import APIRouter

from .notes.views import router as router_notes
from .tasks.views import router as router_tasks

router_v1 = APIRouter()
router_v1.include_router(router_notes, prefix="/notes")
router_v1.include_router(router_tasks, prefix="/tasks")
