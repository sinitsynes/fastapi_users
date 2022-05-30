from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Department_Level, Departments
from ..schemas import Department


class DepDAL():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_level(self):
        new_level = Department_Level()
        self.session.add(new_level)
        await self.session.commit()

    async def add_department(self, request: Department):
        new_dep = Departments(
            department_level=request.department_level,
            description=request.description
        )
        self.session.add(new_dep)
        await self.session.commit()
