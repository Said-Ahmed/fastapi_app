from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .models import operations

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    return 'Hello'
