from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload, subqueryload

from users.models import Department_Level, Departments, UserRoles, User, Role
from users.schemas import Department, User_In_DB, Role_Create

class RoleDAL():
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add_role(self, role: Role_Create):
        new_role = Role(
            name=role.name
        )
        self.session.add(new_role)
        await self.session.commit()

    async def get_all_roles(self):
        query = await self.session.execute(select(Role).order_by(Role.id))
        return query.scalars().all()

    async def get_user_roles(self, user_id, role_id=None, date_created=None):
        filter_queries = [
            (UserRoles.user_id == user_id),
        ]
        if role_id:
            filter_queries.append((UserRoles.role_id == role_id))
        if date_created:
            date_created += '%'
            filter_queries.append((UserRoles.date_created.ilike(date_created)))
        query = await self.session.execute(
            select(UserRoles)
            .filter(*filter_queries)
        )
        roles = query.scalars().all()
        return roles


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
            .where(User.id==user_id)
            .options(selectinload(User.roles))
            .join(Departments, User.department_id == Departments.department_level)
        )
        return query.fetchone()

class DepDAL():
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add_level(self):
        new_level = Department_Level()
        self.session.add(new_level)
        await self.session.commit()

    async def add_department(self, request: Department):
        new_dep = Departments(
            department_level = request.department_level,
            description=request.description
        )
        self.session.add(new_dep)
        await self.session.commit()
