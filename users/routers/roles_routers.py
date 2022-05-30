from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...db_connection import get_session
from ..dals.role_dal import RoleDAL
from ..schemas import Role_Create

roles_router = APIRouter()


@roles_router.post('/add_role')
async def add_role(
    role: Role_Create, session: AsyncSession = Depends(get_session)
):
    role_dal = RoleDAL(session)
    await role_dal.add_role(role)


@roles_router.get('/all_roles')
async def get_all_roles(session: AsyncSession = Depends(get_session)):
    role_dal = RoleDAL(session)
    return await role_dal.get_all_roles()


@roles_router.post('/activate_roles')
async def activate_roles(session=Depends(get_session)):
    role_dal = RoleDAL(session)
    return await role_dal.activate_roles()


@roles_router.get(
    '/users/{user_id}/roles')
async def get_user_roles(
    user_id: int,
    role_id: int | None = None,
    is_active: bool | None = None,
    date_created: str | None = None,
    session: AsyncSession = Depends(get_session)
):
    role_dal = RoleDAL(session)
    return await role_dal.get_user_roles(
        user_id, role_id, is_active, date_created)

    # print(f'user_role {user_role}, role{role}')

    # return UserRoleResponse(
    #     user_id=user_role.user_id,
    #     role_id=user_role.role_id,
    #     is_active=user_role.is_active,
    #     date_created=user_role.date_created,
    #     name=role)
