from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db_connection import get_session
from users.schemas import Role_Create, User_In_DB, UserResponse
from data_access import RoleDAL, UserDAL

router = APIRouter()

@router.post('/add_role')
async def add_role(role: Role_Create, session: AsyncSession = Depends(get_session)):
    role_dal = RoleDAL(session)
    return await role_dal.add_role(role)

@router.get('/all_roles')
async def get_all_roles(session: AsyncSession = Depends(get_session)):
    role_dal = RoleDAL(session)
    return await role_dal.get_all_roles()

@router.post('/add_user')
async def add_user(user: User_In_DB, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    return await user_dal.add_user(user)

@router.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    await user_dal.get_user(user_id)