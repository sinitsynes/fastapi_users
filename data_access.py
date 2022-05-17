from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from users.models import UserRoles, User, Role
from users.schemas import User_In_DB, Role_Create

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


class UserDAL():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user: User_In_DB):
        new_user = User(
            username=user.username,
            password=user.password,
            email=user.email,
        )
        self.session.add(new_user)
        await self.session.flush()
        self.session.refresh(new_user)
        for role_id in user.roles:
            role = UserRoles(user_id=new_user.id, role_id=role_id)
            self.session.add(role)
        await self.session.commit()

    async def get_user(self, user_id: int):
        query = await self.session.execute(select(User).where(User.id==user_id))
        return query.scalars().one_or_none()