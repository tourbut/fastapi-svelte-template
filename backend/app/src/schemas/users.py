from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class UserCreate(CommonBase):
    username: str
    password: str
    email: str

class UserPublic(SQLModel):
    id: int