from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...db_connection import get_session
from ..dals.user_dal import UserDAL
from ..schemas import User_In_DB

user_router = APIRouter()


@user_router.post('/add_user')
async def add_user(
    user: User_In_DB, session: AsyncSession = Depends(get_session)
):
    user_dal = UserDAL(session)
    return await user_dal.add_user(user)


@user_router.get('/users/{user_id}')
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    return await user_dal.get_user(user_id)
