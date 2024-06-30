from app.models import *
from app.src.schemas import users as user_schema
from sqlmodel import Session, select
from app.src.utils.security import get_password_hash

def create_user(*, session: Session, user_create: user_schema.UserCreate) -> User:
    db_obj = User.model_validate(user_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

async def acreate_user(*, session: Session, user_create: user_schema.UserCreate) -> User:
    
    db_obj = User.model_validate(
        user_create, update={"password": get_password_hash(user_create.password)})
    
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj