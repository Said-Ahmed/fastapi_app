from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operations

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    return 'Hello'
