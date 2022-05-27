from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db_connection import get_session
from users.schemas import Department, Role_Create, User_In_DB, UserResponse
from data_access import DepDAL, RoleDAL, UserDAL

router = APIRouter()

@router.post('/add_role')
async def add_role(role: Role_Create, session: AsyncSession = Depends(get_session)):
    role_dal = RoleDAL(session)
    await role_dal.add_role(role)

@router.get('/all_roles')
async def get_all_roles(session: AsyncSession = Depends(get_session)):
    role_dal = RoleDAL(session)
    return await role_dal.get_all_roles()

@router.get('/users/{user_id}/roles')
async def get_user_roles(
    user_id: int,
    role_id: int | None = None,
    session: AsyncSession = Depends(get_session)
):
    role_dal = RoleDAL(session)
    return await role_dal.get_user_roles(user_id, role_id)

@router.post('/add_user')
async def add_user(user: User_In_DB, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    return await user_dal.add_user(user)

@router.get('/users/{user_id}')
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    return await user_dal.get_user(user_id)

@router.post('/add_level')
async def add_level(session: AsyncSession = Depends(get_session)):
    dep_dal = DepDAL(session)
    return await dep_dal.add_level()

@router.post('/add_dep')
async def add_dep(
    request: Department,
    session: AsyncSession = Depends(get_session)
):
    dep_dal = DepDAL(session)
    return await dep_dal.add_department(request)