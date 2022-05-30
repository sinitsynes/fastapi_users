from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User, UserRoles, Departments
from ..schemas import User_In_DB


class UserDAL():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user: User_In_DB):
        new_user = User(
            username=user.username,
            password=user.password,
            email=user.email,
            department_id=user.department_id
        )
        self.session.add(new_user)
        await self.session.flush()
        self.session.refresh(new_user)
        for role_id in user.roles:
            role = UserRoles(user_id=new_user.id, role_id=role_id)
            self.session.add(role)
        await self.session.commit()

    async def get_user(self, user_id: int):
        query = await self.session.execute(
            select(User, Departments.department_level)
            .where(User.id == user_id)
            .options(selectinload(User.roles))
            .join(
                Departments,
                User.department_id == Departments.department_level)
        )
        return query.fetchone()
