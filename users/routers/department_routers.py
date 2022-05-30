from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...db_connection import get_session
from ..dals.dep_dal import DepDAL
from ..schemas import Department

dep_router = APIRouter()


@dep_router.post('/add_level')
async def add_level(session: AsyncSession = Depends(get_session)):
    dep_dal = DepDAL(session)
    return await dep_dal.add_level()


@dep_router.post('/add_dep')
async def add_dep(
    request: Department,
    session: AsyncSession = Depends(get_session)
):
    dep_dal = DepDAL(session)
    return await dep_dal.add_department(request)
