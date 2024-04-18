from typing import Annotated, Type

from fastapi import Depends, HTTPException, Path, status, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.types import ApiCreate, ApiUpdate, ApiItem
from core import db_helper
from core.types import BaseChild


class BaseObjectCRUD:
    def __init__(self, model: Type[BaseChild]):
        self.model = model

    async def get_objects(self, session: AsyncSession) -> list[BaseChild]:
        objs = await session.scalars(
            select(self.model).order_by(self.model.created_at.desc(), self.model.id)
        )
        return list(objs)

    async def get_object(self, session: AsyncSession, obj_id: int) -> BaseChild | None:
        return await session.get(self.model, obj_id)

    async def create_object(
        self,
        session: AsyncSession,
        obj_in: ApiCreate,
    ) -> BaseChild:
        obj = self.model(**obj_in.model_dump())
        session.add(obj)
        await session.commit()
        return obj

    @staticmethod
    async def update_object(
        session: AsyncSession,
        obj: BaseChild,
        obj_update: ApiUpdate,
    ) -> BaseChild:
        for name, val in obj_update.model_dump(exclude_unset=True).items():
            setattr(obj, name, val)
        await session.commit()
        return obj

    @staticmethod
    async def delete_object(session: AsyncSession, obj: BaseChild) -> None:
        await session.delete(obj)
        await session.commit()


class BaseObjectDependencies:
    def __init__(self, crud: BaseObjectCRUD, obj_name: str):
        self.crud = crud
        self.obj_name = obj_name

    async def item_by_id(
        self,
        item_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> BaseChild:
        item = await self.crud.get_object(session, item_id)
        if item:
            return item
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{self.obj_name.title()} {item_id} not found.",
        )


def generate_routes(
    router: APIRouter,
    crud: BaseObjectCRUD,
    dependencies: BaseObjectDependencies,
    model: Type[ApiItem],
):
    @router.get("", response_model=list[model])
    async def get_all(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> list[model]:
        return await crud.get_objects(session)

    @router.get("/{item_id}", response_model=model)
    async def get_one(item: model = Depends(dependencies.item_by_id)) -> model:
        return item

    @router.post("", response_model=model)
    async def create(
        item_in: ApiCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> model:
        return await crud.create_object(session, item_in)

    @router.patch("/{item_id}", response_model=model)
    async def update(
        item_update: ApiUpdate,
        item: model = Depends(dependencies.item_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> model:
        return await crud.update_object(session, item, item_update)

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(
        item: model = Depends(dependencies.item_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> None:
        await crud.delete_object(session, item)
