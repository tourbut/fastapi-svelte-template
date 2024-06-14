from collections.abc import Generator, AsyncGenerator
from typing import Annotated

from sqlmodel import Session,create_engine


from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


SessionDep = Annotated[Session, Depends(get_db)]

SessionDep_async = Annotated[AsyncSession, Depends(get_async_db)]

TokenDep = Annotated[str, Depends(reusable_oauth2)]