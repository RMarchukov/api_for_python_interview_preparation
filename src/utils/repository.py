from sqlalchemy import insert, select, update, delete
from db.db import async_session_maker


class SQLAlchemyRepository:
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def edit_one(self, id: int, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, id: int) -> int:
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=id).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_one(self, **filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            return res
