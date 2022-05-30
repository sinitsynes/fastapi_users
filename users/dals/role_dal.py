from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Role, UserRoles
from ..schemas import Role_Create


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

    async def activate_roles(self):
        await self.session.execute(
            update(UserRoles)
            .values(is_active=True)
        )
        await self.session.commit()

    async def get_user_roles(
        self, user_id=None, role_id=None,
        is_active=None, date_created=None
    ):
        filter_queries = [
            (UserRoles.user_id == user_id),
        ]
        if role_id:
            filter_queries.append((UserRoles.role_id == role_id))
        if date_created:
            filter_queries.append(
                (UserRoles.date_created.ilike('%' + date_created)))
        if is_active:
            filter_queries.append((UserRoles.is_active == is_active))

        query = await self.session.execute(
            select(UserRoles, Role.name)
            .filter(*filter_queries)
            .join(Role, UserRoles.role_id == Role.id)
        )
        return query.fetchall()
