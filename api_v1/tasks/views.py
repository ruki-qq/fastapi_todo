from fastapi import APIRouter, status

router = APIRouter(tags=["tasks"])


@router.get("")
async def get_tasks():
    pass


@router.get("/{task_id}")
async def get_task_by_id(task_id: int):
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task():
    pass


@router.patch("/{task_id}")
async def update_task(task_id: int):
    pass


@router.post("/{task_id}/complete")
async def complete_task(task_id: int):
    pass


@router.post("/{task_id}/delete")
async def delete_task(task_id: int):
    pass
