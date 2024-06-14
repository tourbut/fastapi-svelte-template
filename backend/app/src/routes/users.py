from typing import Any

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep,SessionDep_async
from app.src.crud import users as user_crud
from app.src.schemas import users as user_schema

from app.core.config import settings

router = APIRouter()


@router.post("/signup", response_model=user_schema.UserPublic)
def register_user(*, session: SessionDep, user_in: user_schema.UserCreate) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )

    user = user_crud.create_user(session=session, user_create=user_in)
    
    return user

@router.post("/asignup", response_model=user_schema.UserPublic)
async def aregister_user(*, session: SessionDep_async, user_in: user_schema.UserCreate) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )

    user = await user_crud.acreate_user(session=session, user_create=user_in)
    
    return user